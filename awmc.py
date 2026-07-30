from requests import *
#from webview import *

def health(token):
    token={
        "Authorization":'Bearer '+token
    }
    back=get('https://api.wmc.pub/v1/health',headers=token)
    backjson=back.json()
    print(backjson['status'])


def userdata(token,qrcode):
    token={
        "Authorization":'Bearer '+token
    }
    payload={
        "qrcode":qrcode
    }
    back=post('https://api.wmc.pub/v1/user/data',headers=token,json=payload)
    backchange=back.json()
    print(backchange)