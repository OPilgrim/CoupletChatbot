from django.http import response
import requests
import json
import re

couplet_p = re.compile(r'\“(.*)\”', re.S)
rasabotIP = '45.77.180.242'
rasabotPort = '5005'
rasaURL = "http://{0}:{1}/webhooks/rest/webhook".format(rasabotIP, rasabotPort)

def processSentence(raw_string):
    couplet =  re.findall(couplet_p, raw_string)
    print(couplet)
    couplet_c = '“' + couplet[0] + '”'
    dialog = raw_string.replace(couplet_c, '')
    
    print(couplet_c)
    
    params = {'sender': 'chatbot', 'message': dialog}    
    response = requests.post(
        rasaURL,
        data=json.dumps(params),
        headers={'Content-Type': 'application/json'}
    )

    dialog_return = response.text.encode('utf-8').decode("unicode-escape")
    dialog_return = dialog_return.strip('[]')
    dialog_return = json.loads(dialog_return)
    return dialog_return["text"]