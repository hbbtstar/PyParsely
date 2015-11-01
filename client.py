# low-level client for PyParsely and APIs to interface with
import json
import requests

class Client(object):
    APIKEY = ""
    SECRET = ""
    BASE_URL = "http://api.parsely.com/v2/"
    
    
    def __init__(self, apikey, secret):
        self.APIKEY = apikey
        self.SECRET = secret
        
    def get(self, endpoint, meta=None, value=None, **kwargs):
        ''' gets api results and returns a JSON object. kwargs are interpreted as
        querystring parameters '''
        url = self.BASE_URL + endpoint + "/"
        if meta:
            url += meta + "/"
        if value:
            url += value + "/"
        params = {'apikey': self.APIKEY,'secret': self.SECRET}
        params.update(kwargs)
        response = requests.get(url.rstrip('/'), params=params)
        return response.json()
        
    
        
    