# <p align="center">Michelin-starred restaurants</p>

## <p align="center">Ironhack's Data Analytics Bootcamp Project II: Web Data Pipeline</p>

![Michelin Guide](/images/michelin_2.png)
![Michelin Guide](/images/michelin_3.png)

<p align="center"><i>Choose country and budget, get a Michelin-starred restaurant</i></p>

For this project, I started with a data set of my choice from [kaggle](https://www.kaggle.com/): [Michelin restaurants](https://www.kaggle.com/jackywang529/michelin-restaurants#three-stars-michelin-restaurants.csv). I imported it, used my data wrangling skills to clean it up and built a data pipeline that processes the data and produces a result.

## 

### :woman_cook: STEP 1. Cleaning and enriching the dataset [*cleaningprocess.py*]:

## 

The dataset was cleaned and enriched beforehand:
* NaN values in 'city' variable were filled via **web scraping** with python 'requests' module from https://guide.michelin.com.
* Restaurants minimum and maximum mean price were obtained via **web scraping** from https://guide.michelin.com.
* Prices were converted to euros through the [**Exchangerate API**](https://api.exchangerate-api.com/) and via **web scraping** for those currencies not included in the API.
* Regions were classified into countries through the [**Battuta API**](http://battuta.medunes.net/api) (requires authentication via token).
* Foursquare ID was obtained from the [**Foursquare API**](https://api.foursquare.com) (requires authentication via token).

The final data set contains all the restaurants rated in the Michelin Guide (with 1, 2 or 3 stars) in the following countries/states: Austria, Brazil, Croatia, Czech Republic, Denmark, Finland, Greece, Hong Kong, Hungary, Ireland, Norway, Poland, Singapore, South Korea, Sweden, Taiwan, Thailand, United Kingdom and United States of America.

## 

### :woman_cook: STEP 2. Pipeline usage [*main.py*]:

## 

### INPUT:

The pipeline receives 2 parameters via command-line arguments. I used 'argparse' for this task. This parameters are used to dynamically filter the dataset.

```
main.py [-h] [--state STATE] [--budget BUDGET]
```

Arguments | Function
--------- | -------------
-h, --help | Show help message and exit
--state STATE | State/country you want to consult (default = 'United States of America')
--budget BUDGET | Budget: maximum money you can spend (default = 100)

#### Program call examples:
###### State can be enclosed in quotes or not:
```
python3 main.py --state 'Thailand' --budget 50
python3 main.py --state Thailand --budget 50
```
###### If state's name has spaces, quotes must be used:
```
python3 main.py --state 'United States of America' --budget 100
```

Valid states: Austria, Brazil, Croatia, Czech Republic, Denmark, Finland, Greece, Hong Kong, Hungary, Ireland, Norway, Poland, Singapore, South Korea, Sweden, Taiwan, Thailand, United Kingdom and United States of America.

## 

### OUTPUT:

The program returns a restaurant chosen at random from among those that meet the constraints determined by the input parameters. The pipeline also creates some reports containing valuable data from the dataset:
* Text report printed in console 'stdout': Contains basic statistics and data aggregations.
* Pie charts (Michelin stars and cuisine types in the selected state).
* PDF report.
* Sending PDF as email attachment (with pie charts inside the pdf file).

Reports are dynamically enriched via **web scraping** from https://guide.michelin.com and through the [Foursquare API](https://api.foursquare.com) (requires authentication via token), in order to get: Restaurant services, opening days and hours and a recommendation of a nearby cinema to go to after lunch/dinner.

## 

<p align="center"><img  src="https://github.com/Masdevallia/data-analysis-pipeline/blob/master/images/input_output.png" width="700"></p>

## 

### :woman_cook: Deliverables:

## 

* *cleaningprocess.py*: Contains all Python code and commands used in the importing, cleaning, manipulation, and exporting of the final cleaned and enriched data set.
* *main.py*: Contains the pipeline.
* *images* folder: Contains some images displayed in *readme.md* and in the PDF reports.
* *input* folder:
    * Initial data sets (*one-star-michelin-restaurants.csv*, *two-stars-michelin-restaurants.csv*, *three-stars-michelin-restaurants.csv*)
    * Cleaned and enriched final data set (*cleaned_enriched_df.csv*)
* *output* folder:
    * Pie charts
    * PDF reports
* *src* folder: Contains functions I have imported and used in the pipeline:
    * *apy.py*: functions related to APIs' usage.
    * *clean.py*: functions ralated to data cleaning/wrangling.
    * *datavisualization.py*: functions related to exploratory data visualization (charts).
    * *mail.py*: functions related to generating the email report.
    * *pdf.py*: functions related to generating the PDF report.
    * *webscraping.py*: functions related to the web scraping process.

![Michelin Guide](/images/michelin_petit.png)