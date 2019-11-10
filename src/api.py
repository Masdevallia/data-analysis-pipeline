
# API related functions:

def exchangerate_api_request(currency):
    # Requests to exchangerate-api
    # currency must be a string of three capital letters: e.g. EUR
    import requests
    url = "https://api.exchangerate-api.com/v4/latest/{}".format(currency)
    res = requests.get(url)
    return res


def battuta_request_authorized(resource):
    # Requests to battuta(countries/regions/cities)-api
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
