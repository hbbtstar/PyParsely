from client import Client

class Post(object):
    
    def __unicode__(self):
        return self.title + "({})".format(self.url)
        
    def __init__(self, client, post_url):
        self.url = post_url
        self._client = client
        post_resp = self._client.get('analytics', 'post', 'detail', url=post_url)
        for key, result in post_resp['data'][0].items():
            setattr(self, key, result)
        self.hits = self._hits
        self.thumbnail = self.thumb_url_medium
        self.image = self.image_url
        
        
        