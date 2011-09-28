#!/usr/bin/env python
import web
import os
import json

from traceback import print_exc


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
        except TypeError:
            msg = 'HTTP 400 - Bad Request'
            if getattr(controller, '__doc__', False):
                msg += '\n' + controller.__doc__
            
            print_exc()
            raise self.badrequest(msg)
        
        if isinstance(res, dict):
            web.header('Content-Type', 'application/json')
            res = json.dumps(res)
            
        
        return res
    
        
    def badrequest(self, message):
        return web.HTTPError('400 Bad Request', {'Content-Type': 'text/plain'}, message)




urls = (
  '/(.*)', 'FrontController'
)

app = web.application(urls, globals())
if __name__ == '__main__':
    with open(os.path.expanduser('~/environment.json'), 'w') as f:
        json.dump(dict(DOTCLOUD_DATA_MONGODB_URL = 'localhost'), f)
    
    app.run()
else:
    with open(os.path.expanduser('~/environment.json')) as f:
        env = json.load(f)
        web.DOTCLOUD_DATA_MONGODB_URL = env['DOTCLOUD_DATA_MONGODB_URL']
    web.config.debug = False
    application = app.wsgifunc()
