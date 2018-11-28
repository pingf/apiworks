
from apiworks.server.wsgi.router import Router

router = Router()

@router.route("^/favicon.ico", mode='group')
def test():
    return 'icon'

@router.route("^/hello")
def index():
    return 'world'

if __name__ == '__main__':
    pass