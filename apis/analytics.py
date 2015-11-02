''' Analytics endpoint API '''
from lib.api_objects import Post
class AnalyticsAPI(object):
    
    def __init__(self, client):
        self._client = client
        
    def posts(self):
        ''' returns a list of posts '''
        pass
    
    def post(self, post_url):
        ''' returns a single post '''
        return Post(self._client, post_url)
    