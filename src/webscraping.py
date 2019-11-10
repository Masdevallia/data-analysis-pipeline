
# Web scraping related functions:

def get_soup(url):
    # get soup from url
    import requests
    from bs4 import BeautifulSoup
    res = requests.get(url)
    html = res.text
    return BeautifulSoup(html, 'html.parser')

