import web
import json


class Heatmap:
    """
    /heatmap?video=<video_id>&[getkey=1|0]
    """
    def GET(self, video, getkey=False):
        return '%r %r' % (video, getkey)

class Echo:
    def GET(self, **kwargs):
        return kwargs
