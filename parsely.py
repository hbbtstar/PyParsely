# simple wrapper for Parsely API
from client import Client

class PyParsely(object):

    def __init__(self, apikey, secret):
        self._client = Client(apikey, secret)
        
    