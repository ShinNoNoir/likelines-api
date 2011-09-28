import web
import json


class Heatmap:
    """
    /heatmap?video=<video_id>&[getkey=1|0]
    """
    def GET(self, video, getkey=False):
        res = {}
        res['heatmap'] = []
        if getkey:
            res['key'] = None
        return res

class Echo:
    def GET(self, **kwargs):
        res = dict(kwargs)
        
        try:
            from pymongo import Connection
            conn = Connection(web.env['DOTCLOUD_DATA_MONGODB_URL'])
            db = conn.test_db
            res['db.foos'] = db.foos.find()
        except:
            import traceback
            res['exc'] = traceback.format_exc()
        
        return res
