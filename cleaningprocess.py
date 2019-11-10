
# Importing packages and loading env:
import pandas as pd
import numpy as np
import re
import requests
import json
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
from src.api import exchangerate_api_request
from src.api import battuta_request_authorized
from src.api import foursquare_request_venues_authorized
from src.api import foursquare_menu_hours_authorized
from src.api import foursquare_get_id_authorized
from src.webscraping import get_soup
from src.clean import resub_list

# Importing the 3 dataframes:
df_1star = pd.read_csv('./input/one-star-michelin-restaurants.csv')
df_2star = pd.read_csv('./input/two-stars-michelin-restaurants.csv')
df_3star = pd.read_csv('./input/three-stars-michelin-restaurants.csv')

# Adding column 'stars':
df_1star['stars'] = [1]*df_1star.shape[0]
df_2star['stars'] = [2]*df_2star.shape[0]
df_3star['stars'] = [3]*df_3star.shape[0]

# Putting the 3 dataframes together:
df = pd.concat([df_1star, df_2star,df_3star], ignore_index=True, sort=False)

# Deleting columns that I will not need in my program: Award year & zipCode:
df = df.drop(['zipCode','year'], axis=1)

#..........................................................................................

# Filling NaN values in 'city' column:
# Web scraping https://guide.michelin.com to get cities
city_list = []
for e in df['url'][df['city'].isnull() == True]:
    soup = get_soup(e)
    city_list.append(re.sub('\n|\s','', soup.select('.restaurant-details__heading--list')[0].text).split(',')[-2][:8])
# Filling NaN values:
index_city = 0
for i in df[df['city'].isnull() == True].index:
    df.at[i,'city'] = '{} {}'.format(city_list[index_city][:4],city_list[index_city][4:])
    index_city += 1

#..........................................................................................

# Filling NaN values in 'price' column:
# Web scraping https://guide.michelin.com to get prices
prices_rest_list = []
for i in range(len(df)):
    soup = get_soup(df['url'][i])
    prices = soup.select('.restaurant-details__heading-price')
    if prices:
        prices_rest_list.append([df['name'][i], re.sub('\n|\s','',prices[0].text).split('•')[0]])
restaurants = [e[0] for e in prices_rest_list]
price = [e[1] for e in prices_rest_list]

# Deleting thousands separator:
correct_price = resub_list(price,',','')

# Some restaurants don't have currency information. Deleting them:
rows_to_delete = [bool(re.match('[A-Z]{3}', correct_price[i][-3:])) for i in range(len(correct_price))]
restaurants = [restaurants[i] for i in range(len(restaurants)) if rows_to_delete[i] == True]
correct_price = [correct_price[i] for i in range(len(correct_price)) if rows_to_delete[i] == True]

# Separating min price values, max price values and currency:
correct_price_2 = []
for i in range(len(correct_price)):
    correct_price_2.append('{} {}'.format(correct_price[i][:-3],correct_price[i][-3:]))
correct_price_3 = list(map(lambda x: x.split(' '), correct_price_2))
price = [e[0] for e in correct_price_3]
currency = [e[1] for e in correct_price_3]
price_minmax = list(map(lambda x: x.split('-'), price))
price_min = [int(e[0]) for e in price_minmax]
price_max = [int(e[1]) for e in price_minmax]

# Changing all prices to EUR using an API:
exchangerate = exchangerate_api_request('EUR').json()

# The API doesn't support MOP: MOP TO HKD through Web Scraping:
soup = get_soup('https://en.wikipedia.org/wiki/Macanese_pataca')
mop_hkd = float(soup.select('#mw-content-text > div > table:nth-child(1) > tbody > tr:nth-child(26) > td')[0].text[-4:])
# 'HKD 1 = MOP 1.03'

price_min_eur = []
price_max_eur = []
i = 0
for e in currency:
    if e == 'MOP':
        price_min_eur.append(price_min[i]/mop_hkd/exchangerate['rates']['HKD'])  
        price_max_eur.append(price_max[i]/mop_hkd/exchangerate['rates']['HKD'])
    else:
        price_min_eur.append(price_min[i]/exchangerate['rates'][e])
        price_max_eur.append(price_max[i]/exchangerate['rates'][e])
    i += 1

df['min_price_EUR'] = [np.nan]*len(df)
df['max_price_EUR'] = [np.nan]*len(df)

for i in range(len(df)):
    for j in range(len(restaurants)):
        if df.at[i,'name'] == restaurants[j]:
            df.at[i,'min_price_EUR'] = price_min_eur[j]
            df.at[i,'max_price_EUR'] = price_max_eur[j]
            
# Deleting column 'price':
df = df.drop(['price'], axis=1)

# Deleting rows with missing 'price' values
df_final = df[~df['max_price_EUR'].isnull()]
df_final.reset_index(drop=True, inplace=True)

# Deleting otliers:
df_price = df_final[['min_price_EUR','max_price_EUR']]
stats = df_price.describe().transpose()
stats['IQR'] = stats['75%'] - stats['25%']

outliers = pd.DataFrame(columns=df_price.columns)
for col in stats.index:
    iqr = stats.at[col,'IQR']
    cutoff = iqr * 15 # Multiplying by 15 because I'm interested in taking out only very exorbitant outliers
    lower = stats.at[col,'25%'] - cutoff
    upper = stats.at[col,'75%'] + cutoff
    results = df_price[(df_price[col] < lower) | 
                   (df_price[col] > upper)].copy()
    results['Outlier'] = col
    outliers = outliers.append(results)

rowstodelete = list(set(outliers.index))

df_final.drop(rowstodelete, axis = 0, inplace=True)
df_final.reset_index(drop=True, inplace=True)

# Once the NaNs deleted, I can set the column type to 'int':
df_final['min_price_EUR'] = df_final['min_price_EUR'].astype('int')
df_final['max_price_EUR'] = df_final['max_price_EUR'].astype('int')

#..........................................................................................

# Standardizing 'cuisine' column:
for i in range(len(df_final)):
    df_final.at[i,'cuisine'] = df_final.at[i,'cuisine'].capitalize()

# Standardizing 'city' column:
for i in range(len(df_final['city'])):
    if len(re.findall('Paulo', df_final.at[i,'city'])) > 0:
        df_final.at[i,'city'] = re.sub(df_final.at[i,'city'],'São Paulo',df_final.at[i,'city'])
for i in range(len(df_final['city'])):
    if len(re.findall('Janeiro', df_final.at[i,'city'])) > 0:
        df_final.at[i,'city'] = re.sub(df_final.at[i,'city'],'Rio de Janeiro',df_final.at[i,'city'])

#..........................................................................................

# Classifying regions into countries (according to battuta API):
# battuta_request_authorized('/quota/?').json()

regions = list(set(df_final['region']))

battuta_states = []
for e in regions:
    battuta_states.append([e,battuta_request_authorized('/country/search/?country={}&'.format(e)).json()])

df_final['state'] = ['state']*len(df_final)

states = []
for i in range(len(battuta_states)):
    if len(battuta_states[i][1]) > 0:
        states.append(battuta_states[i][0])
        
for i in range(len(df_final)):
    for country in states:
        if df_final.at[i,'region'] == country:
            df_final.at[i, 'state'] = country

remaining_regions = [e[0] for e in battuta_states if e[0] not in states]

# Due to the particularities and limitations of the API (max 500 requests), I have to make these last
# substitutions a bit manually...:
remaining_states = []
for e in remaining_regions:
    if e == 'California':
        remaining_states.append(battuta_request_authorized('/country/search/?region={}&'.format(e)).json()[1]['name'])
    elif len(battuta_request_authorized('/country/search/?city={}&'.format(e)).json()) > 0:
        remaining_states.append(battuta_request_authorized('/country/search/?city={}&'.format(e)).json()[0]['name'])
    else:
        remaining_states.append(e)
remaining_states[4] = 'United States of America'
remaining_states[6] = 'United States of America'
remaining_states[7] = 'United States of America'

for i in range(len(df_final)):
    for j in range(len(remaining_regions)):
        if df_final.at[i,'region'] == remaining_regions[j]:
            df_final.at[i, 'state'] = remaining_states[j]

#..........................................................................................

# df_final.drop_duplicates() # 665 rows: There are not duplicates

cols = ['name','state','region','city','latitude','longitude','cuisine','stars','min_price_EUR','max_price_EUR','url']
df_final = df_final[cols]

#..........................................................................................

# Adding some more information from foursquare API:

restaurants_id = []
restaurants_name = []
restaurants_address = []
for i in range(len(df_final)):
    data = foursquare_get_id_authorized(df_final['name'][i],df_final['latitude'][i],df_final['longitude'][i])['response']['venues']
    if data:
        restaurants_id.append(data[0]['id'])
        restaurants_name.append(data[0]['name'])
        restaurants_address.append(data[0]['location']['formattedAddress'])
    else:
        restaurants_id.append('not found')
        restaurants_name.append('not found')
        restaurants_address.append('not found')

df_final['foursquare_id'] = restaurants_id
df_final['foursquare_name'] = restaurants_name
df_final['foursquare_address'] = [e if e == 'not found' else e[0] for e in restaurants_address]

#..........................................................................................

# df_final.to_csv('./input/cleaned_enriched_df.csv', index=False)
# df_final = pd.read_csv('./input/cleaned_enriched_df.csv')

# display(df_final.head())