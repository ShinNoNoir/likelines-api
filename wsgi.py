#!/bin/env python
import web
import json
from cgi import parse_qs

from api import Heatmap, Echo


class FrontController:
    CONTROLLERS = {
        'heatmap' : Heatmap,
        'echo': Echo
    }
    
    def GET(self, path):
        if not path in FrontController.CONTROLLERS:
            raise web.notfound('HTTP 404 - Unknown Request')
        
        controller = FrontController.CONTROLLERS[path]
        handler = controller()
        query = dict(web.input())
        
        try:
            res = handler.GET(**query)
            
            if isinstance(res, dict):
                web.header('Content-Type', 'application/json')
                res = json.dumps(res)
            
            return res
            
        except TypeError:
            msg = 'HTTP 400 - Bad Request'
            if getattr(controller, '__doc__', False):
                msg += '\n' + controller.__doc__
                
            raise self.badrequest(msg)
        
        
    def badrequest(self, message):
        return web.HTTPError('400 Bad Request', {'Content-Type': 'text/plain'}, message)

urls = (
  '/(.*)', 'FrontController'
)

app = web.application(urls, globals())
if __name__ == '__main__':
    app.run()
else:
    web.config.debug = False
    application = app.wsgifunc()



#RESPONSE_JSON = [('Content-type', 'application/json')]
#RESPONSE_TXT = [('Content-type', 'text/plain')]


#def application(environ, start_response):
#    query = parse_qs(environ['QUERY_STRING'])
#    path = parse_qs(environ['PATH_INFO'])
#    
#    response_headers = RESPONSE_TXT
#    response_body = ''
#    
#    if path in routes:
#        try:
#            response_status = '200 OK'
#            response_body = routes[path](environ)
#            response_headers = RESPONSE_JSON
#        except Exception as e:
#            response_status = '500'
#            response_body = repr(e)
#    else:
#        response_status = '404 NotFound'
#        response_body = 'boo'
    
#    
#    
#    response_headers = [('Content-type', 'text/plain')]
#    start_response(response_status, response_headers)
#    return [response_body]

    #return ['Hello world!\n'] + ['{0}={1}\n'.format(k,environ[k])
    #                             for k in sorted(environ)] + [repr(query)]

