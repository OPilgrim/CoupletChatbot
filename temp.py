# 怎么连接服务获取对联

def get_couplet_right(couplet_up):
    import requests
    from urllib import parse,request
    from couplet_dialog.models import Dialog_api
    
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    url = Dialog_api.object.filter(dialog_core='couplet')   # 'http://139.9.113.51:5000/CoupletAI/'
    params = {'couplet_up':couplet_up}
    params = parse.urlencode(params)
    response = request.Request(url='%s%s%s' % (url,'?',params),headers=headers)
    response = request.urlopen(response)
    response = response.read()
    return response.decode('utf8')