import functools
import re

from apiworks.server.wsgi.raw_app import raw_app
from apiworks.server.wsgi.status import status
from apiworks.server.wsgi.matcher import Match, NotFound



class Router(object):
    def __init__(self, app=None, rules=None, omissions=None, validator=None):
        self.app = app
        self.rules = rules if rules else []
        self.omissions = omissions
        # this is the default validator
        self.validator = validator

    def route(self, pattern, methods=["GET"], mode='groupdict', validator=None):
        def decor(core):
            regex = re.compile(pattern)
            app = functools.partial(raw_app, core=core)
            print(app,core,regex,pattern,methods, validator, mode)
            self.rules.insert(0, (
                app, core, regex, pattern, methods, validator or self.validator, mode
            ))
            return self
        return decor

    def resolve(self, method, path):
        tried = []
        # original_path = path
        for (app, core, regex, pattern, methods, validator, mode) in self.rules:
            if method in methods:
                match = regex.match(path)
                restpath = regex.sub('', path)
                params = dict(match=match, path=path, regex=regex, pattern=pattern,
                              method=method, methods=methods, restpath=restpath, mode=mode)
                if match:
                    self.build_params(match, params, validator)
                    return Match(app=app, **params)
                else:
                    tried.append(params)

        raise NotFound(self, tried)

    def build_params(self, match, params, validator):
        args, kwargs = self.args_from_match(match)
        params['args'] = args
        params['kwargs'] = kwargs
        if validator:
            if len(args)>0:
                if not isinstance(validator, list):
                    validator = [validator]
                self.validate_for_args(args, validator, params)
            elif len(kwargs)>0:
                self.validate_for_kwargs(kwargs, validator, params)

    def args_from_match(self, match):
        kwargs = match.groupdict()

        if kwargs:
            args = ()
        else:
            kwargs = {}
            args = match.groups()
        return args, kwargs

    def validate_for_kwargs(self, kwargs, validator, params):
        validated = {}
        for k,v in kwargs:
            valid = validator.get(k)
            if valid:
                validated[k] = valid(v)
            else:
                validated[k] = v
        params['kwargs'] = validated

    def validate_for_args(self, args, validator, params):
        validated = []
        for i,arg in enumerate(args):
            if i > len(validator):
                valid = validator[i%len(validator)]
            else:
                valid = validator[i]
            validated.append(valid(args[i]))
        params['args'] = validated

    def path_info(self, environ):
        return environ['PATH_INFO']

    def __call__(self, environ, start_response, path=None):
        method = environ['REQUEST_METHOD']
        path = path or self.path_info(environ)
        result = self.resolve(method, path)
        if result.app:
            environ['wsgi.args'] = result.args
            environ['wsgi.kwargs'] = result.kwargs
            environ['wsgi.restpath'] = result.restpath
            try:
                response =  result.app(environ, start_response)
            except NotFound as e:
                not_found_func = self.omissions
                if not_found_func is None:
                    raise e
                app = functools.partial(raw_app, core=not_found_func)
                response = app(environ, start_response)

            return response
