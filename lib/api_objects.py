from client import Client

class Post(object):
    
    def __unicode__(self):
        return self.title + "({})".format(self.url)
        
    def __repr__(self):
        return "Post('{}')".format(self.url)
        
    def __init__(self, client, post_url, access=False, **kwargs):
        self.url = post_url
        self._client = client
        if access:
            self.access_API()
            self.accessed = True
        else:
            self.accessed = False
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == "thumb_url_medium":
                    self.thumbnail = self.thumb_url_medium
                if key == "image_url":
                     self.image = self.image_url
                if key == "hits":
                    self.hits = self._hits
        
    # only access the API if the post ends up being used- this lets people
    # work with URLs of posts without having to query the API
    def __getattr__(self, item):
        if self.accessed or item == "url":
            return object.__getattribute__(self, item)
        elif self.accessed == False:
            self.access_API()
            return object.__getattribute__(self, item)
        else:
            return object.__getattr__(self, item)
        
    def access_API(self):
        post_resp = self._client.get('analytics', 'post', 'detail', url=self.url)
        for key, result in post_resp['data'][0].items():
            setattr(self, key, result)
        self.hits = self._hits
        self.thumbnail = self.thumb_url_medium
        self.image = self.image_url
        self.accessed = True
        
        
        