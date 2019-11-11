
# API related functions:

def exchangerate_api_request(currency):
    '''
    Requests to exchangerate-api
    currency must be a string of three capital letters: e.g. EUR
    '''
    import requests
    url = "https://api.exchangerate-api.com/v4/latest/{}".format(currency)
    res = requests.get(url)
    return res


def battuta_request_authorized(resource):
    '''
    Requests to battuta(countries/regions/cities)-api
    '''
    import requests
    import os
    from dotenv import load_dotenv
    load_dotenv()
    authToken = os.getenv("BATTUTA_API_KEY")
    if not authToken:
        raise ValueError("Missing API key")
    else:
        print("Battuta API key: ", authToken[0:4], '[...]')
    url = "http://battuta.medunes.net/api{}key={}".format(resource,authToken)
    res = requests.get(url)
    return res


def foursquare_request_venues_authorized(request, latitude, longitude, myquery, limit=1, radius = 1000):
    '''
    Requests to foursquare-api:
    Input:
    request: string:
    1) 'search': Returns a list of venues near the current location, matching a search term.
    2) 'explore': Returns a list of recommended venues near the current location.
    ll = '40.7243,-74.0018'.
    query = a search term to be applied against venue names: 'coffee'.
    limit = number of results to return, up to 50. Defaults to 1.
    radius = Limit results to venues within this many meters of the specified location. Defaults to 1km.
    '''
    import json
    import requests
    import os
    from dotenv import load_dotenv
    load_dotenv()
    url = 'https://api.foursquare.com/v2/venues/{}'.format(request)
    params = dict(
        client_id = os.getenv("FOURSQUARE_CLIENT_ID"),
        client_secret = os.getenv("FOURSQUARE_CLIENT_SECRET"),
        v='20180323', # version parameter
        ll='{},{}'.format(latitude,longitude),  
        query= myquery,
        limit=limit,
        radius=radius
    )
    resp = requests.get(url=url, params=params)
    return json.loads(resp.text)


def foursquare_menu_hours_authorized(request, venue_id):
    '''
    Requests to foursquare-api:
    input = venue id = e.g. AVNU234.
    'menu': Returns menu information for a venue.
    'hours': Returns hours for a venue.
    '''
    import json
    import requests
    import os
    from dotenv import load_dotenv
    load_dotenv()
    url = 'https://api.foursquare.com/v2/venues/{}/{}'.format(venue_id, request)
    params = dict(
        client_id = os.getenv("FOURSQUARE_CLIENT_ID"),
        client_secret = os.getenv("FOURSQUARE_CLIENT_SECRET"),
        v='20180323' # version parameter
    )
    resp = requests.get(url=url, params=params)
    return json.loads(resp.text)


def foursquare_get_id_authorized(query, latitude, longitude, limit = 1):
    '''
    get the restaurant id by its name
    '''
    import json
    import requests
    import os
    from dotenv import load_dotenv
    load_dotenv()
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id = os.getenv("FOURSQUARE_CLIENT_ID"),
        client_secret = os.getenv("FOURSQUARE_CLIENT_SECRET"),
        v='20180323', # version parameter
        ll='{},{}'.format(latitude,longitude),
        query = query,
        limit = limit
    )
    resp = requests.get(url=url, params=params)
    return json.loads(resp.text)
