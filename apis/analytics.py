''' Analytics endpoint API '''
from lib.api_objects import Post
class AnalyticsAPI(object):
    

        
    def __init__(self, client):
        self._client = client
        
    def posts(self):
        ''' returns a list of posts '''
        post_list = []
        posts_resp = self._client.get('analytics', 'posts')
        print posts_resp['data']
        for entry in posts_resp['data']:
            post_list.append(Post(self._client, entry['url'], **entry))
        return post_list
            
            
        
    
    def post(self, post_url):
        ''' returns a single post '''
        return Post(self._client, post_url)
        
    