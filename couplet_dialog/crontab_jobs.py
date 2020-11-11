# 定时任务
# 从redis提取新语料到sqlite
def redis_to_sqlite():
    import redis
    from django_redis import get_redis_connection
    from couplet_dialog.models import Couplet_warehouse
    '''
    要求setting.py：
    CACHES = {
        "default":{
            "BACKEND":"django_redis.cache.RedisCache",
            "LOCATION":"redis://127.0.0.1:6379",
            "OPTIONS":{
                "CLIENT_CLSAA":"diango_redis.client.DefaultClient",
                "CONNECTION_POOL_KWARGS":{"max_connections":100},
                # "PASSWORD":'121352',
            }
        }
    }
    '''
    conn_redis = get_redis_connection()
    pipe = conn_redis.pipeline()
    pipe_size = 100000
    keys = conn_redis.keys()
    key_list = []
    index = 0
    for key in keys():
        key_list.append(key)
        pipe.get(key)
        if index < pipe_size:
            index += 1
        else:
            for (k, v) in zip(key_list, pipe.execute()):
                # 判断status 和 quality，只拉取通过和评级好的语料
                if condition:   # !!!!!!!condition不知道怎么写，或许知道redis的结构会对我有帮助
                    # 连接sqlite
                    couplet = Couplet_warehouse(couplet_left=string1, couplet_right=string2)  # !!!!!!!
                    # 数据插入
                    couplet.save()
                    # redis里该条语料记录“已处理”
            index = 0
            key_list = []
     
    for (k, v) in zip(key_list, pipe.execute()):
        # 判断status 和 quality，只拉取通过和评级好的语料
        if condition:   # !!!!!!!condition不知道怎么写，或许知道redis的结构会对我有帮助
            # 连接sqlite
            couplet = Couplet_warehouse(couplet_left=string1, couplet_right=string2)  # !!!!!!!
            # 数据插入
            couplet.save()
            # redis里该条语料记录“已处理”