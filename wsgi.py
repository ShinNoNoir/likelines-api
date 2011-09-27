from api import foo
from cgi import parse_qs

import json

RESPONSE_JSON = [('Content-type', 'application/json')]
RESPONSE_TXT = [('Content-type', 'text/plain')]

routes = {
    '/foo' : foo
}

def application(environ, start_response):
    query = parse_qs(environ['QUERY_STRING'])
    path = parse_qs(environ['PATH_INFO'])
    
    response_headers = RESPONSE_TXT
    response_body = ''
    
    if path in routes:
        try:
            response_status = '200 OK'
            response_body = routes[path](environ)
            response_headers = RESPONSE_JSON
        except Exception as e:
            response_status = '500'
            response_body = repr(e)
    else:
        response_status = '404 NotFound'
        response_body = 'boo'
    
    
    
    response_headers = [('Content-type', 'text/plain')]
    start_response(response_status, response_headers)
    return [response_body]

    #return ['Hello world!\n'] + ['{0}={1}\n'.format(k,environ[k])
    #                             for k in sorted(environ)] + [repr(query)]

