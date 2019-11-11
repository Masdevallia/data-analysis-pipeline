# Michelin-starred restaurants

## Ironhack's Data Analytics Bootcamp Project II: Web Data Pipeline

![Michelin Guide](/images/michelin_2.png)
![Michelin Guide](/images/michelin_3.png)

For this project, I started with a data set of my choice from [kaggle](https://www.kaggle.com/): [Michelin restaurants](https://www.kaggle.com/jackywang529/michelin-restaurants#three-stars-michelin-restaurants.csv). I imported it, used my data wrangling skills to clean it up and built a data pipeline that processes the data and produces a result.

The data set contains all the restaurants rated in the Michelin Guide in the following countries/states: Austria, Brazil, Croatia, Czech Republic, Denmark, Finland, Greece, Hong Kong, Hungary, Ireland, Norway, Poland, Singapore, South Korea, Sweden, Taiwan, Thailand, United Kingdom and United States of America.

### :woman_cook: Methods:

[...]

### :woman_cook: Pipeline usage:

Get a Michelin Restaurant from two arguments: state and budget.

main.py [-h] [--state STATE] [--budget BUDGET]

Optional arguments | Function
------------------ | -------------
-h, --help | Show help message and exit
--state STATE | State/country you want to consult (default = 'United States of America')
--budget BUDGET | Budget: maximum money you can spend (default = 100)

Examples:
With quotes or without:
* *python3 main.py --state 'Thailand' --budget 50*
* *python3 main.py --state Thailand --budget 50*
If the name has spaces, quotes must be used:
* *python3 main.py --state 'United States of America' --budget 100*

### :woman_cook: Deliverables:

* *input* folder:
    * Initial data sets (*one-star-michelin-restaurants.csv*, *two-stars-michelin-restaurants.csv*, *three-stars-michelin-restaurants.csv*)
    * Cleaned and enriched final data set (*cleaned_enriched_df.csv*)
* *output* folder:
    * Pie charts
    * [...]
* *src* folder: Contains functions I have imported and used in the pipeline:
    * *clean.py*: functions ralated to data cleaning/wrangling.
    * *apy.py*: functions related to APIs' usage.
    * *webscraping.py*: functions related to web scraping process.
    * *datavisualization.py*: functions related to exploratory data visualization (charts).
* *images* folder: Contains some images displayed in *readme.md*.
* *cleaningprocess.py* contains all Python code and commands used in the importing, cleaning, manipulation, and exporting of the final data set.
* *main.py* contains the pipeline.
* Jupyter notebook (*Tests_Data_cleaning.ipynb*, *Tests_Others.ipynb* and *Tests_Pipeline.ipynb*) was used just for testing the code.

### :woman_cook: Obstacles encountered and lessons learned:

[...]

![Michelin Guide](/images/michelin_petit.png)