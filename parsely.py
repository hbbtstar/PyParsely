# simple wrapper for Parsely API
from client import Client
from apis.analytics import AnalyticsAPI

class PyParsely(object):

    def __init__(self, apikey, secret):
        self._client = Client(apikey, secret)
        self.analytics = AnalyticsAPI(self._client)
        
    