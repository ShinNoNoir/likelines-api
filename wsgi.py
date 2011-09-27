#!/bin/env python
import web
import json

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
