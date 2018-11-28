
class NotFound(Exception):
    def __init__(self, router, tried):
        self.router = router
        self.tried = tried

    def __str__(self):
        return "<RouteNotFound tried: %r>" % (self.tried)

class Match(object):
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            self.__setattr__(k,v)
