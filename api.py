import web
import json

def Connection():
    import pymongo
    return pymongo.Connection(web.DOTCLOUD_DATA_MONGODB_URL)
    
    
class Heatmap:
    """
    /heatmap?video=<video_id>&[getkey=1|0]
    """
    def GET(self, video, getkey=False):
        res = {}
        res['heatmap'] = []
        if getkey:
            res['key'] = getkey 
        return res

class Echo:
    def GET(self, **kwargs):
        res = dict(kwargs)
        
        try:
            conn = Connection()
            db = conn.test_db
            res['db.foos'] = foos = []
            for foo in db.foos.find():
                del foo['_id']
                foos.append(foo)
        
        except:
            import traceback
            res['exc'] = traceback.format_exc()
        
        return res
