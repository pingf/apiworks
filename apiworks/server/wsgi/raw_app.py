
def raw_app(environ, start_response,  core=None):
    if isinstance(core, Router):
        restpath = environ['wsgi.restpath']
        return core(environ, start_response, path=restpath)

    args = environ['wsgi.args']
    kwargs = environ['wsgi.kwargs']

    result = core(*args, **kwargs)

    return_value = None
    if isinstance(result, tuple):
        if len(result) == 2:
            start_response(status[result[1]], [('Content-type', 'text/html')])
        elif len(result)>2:
            headers = []
            for k,v in result[2].items():
                headers.append((k,v))
            start_response(status[result[1]], headers)
        return_value = [str(result[0]).encode('utf8')]
    start_response("200 OK", [('Content-type', 'text/html')])
    return_value = [str(result).encode('utf8')]
    return return_value