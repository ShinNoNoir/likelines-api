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
        res['web.env'] = web.env
        return res
