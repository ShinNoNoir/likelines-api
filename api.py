# Written by Raynor Vliegendhart
# see LICENSE for license information

import web
import time

def Connection():
    import pymongo
    return pymongo.Connection(web.DOTCLOUD_DATA_MONGODB_URL)


def UserId():
    import uuid
    str(uuid.uuid4())
    
    user_id = web.cookies(user_id=None).user_id
    if user_id is None:
        user_id = str(uuid.uuid4())
        web.setcookie('user_id', user_id,  31556926)
    
    return user_id


class Heatmap:
    """
    /heatmap?video=<url>&[getkey=1|0]
    
    Returns:
    {
      "heatmap": <heatmap>,
      "interaction_key": <interaction_key>  
    }
    """
    def GET(self, video, getkey=False):
        # TODO: URL normalizer? 
        
        conn = Connection()
        likes_db = conn.likes
        played_fragments = conn.played_fragments
        
        # TODO: "schema"?
        
        heatmap = []
        for like in likes_db.find({'video': video}):
            pass # TODO: Aggregate
        
        for fragments in played_fragments.find():
            pass # TODO: Aggregate 
        
        
        res = {}
        res['heatmap'] = heatmap
        if getkey:
            interaction_keys_db = conn.interaction_keys
            # For now, don't require a key:
            res['key'] = 'NoKeyNeeded'
        
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
            
            res['user_id'] = UserId()
        
        except:
            import traceback
            res['exc'] = traceback.format_exc()
        
        return res
