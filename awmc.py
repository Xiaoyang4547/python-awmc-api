from requests import *
#from webview import *
import json

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
    data=json.loads(backchange['msg'])
    print(data)
    print('用户基本信息:')
    print('用户ID:'+str(data['userId']))
    print('用户名称:'+str(data["userData"]['userName']))
    #封禁检测
    if data['banState']==0:
        print('封禁状态:正常')
    elif data['banState']==1:#猜的
        print('封禁状态:bs1')
    elif data['banState']==2:#猜的
        print('封禁状态:bs2')
    else:
        print('封禁状态:未知')
    print('总Rating:'+str(data["userData"]['playerRating']))
    print('旧版本Rating(B35):'+str(data["userData"]['playerOldRating']))
    print('新版本Rating(B15):'+str(data["userData"]['playerNewRating']))
    print('段位:'+str(data['userData']['courseRank'])+'段')
    print('收藏品信息:')
    print('头像ID:'+str(data['userData']['iconId']))
    print('姓名框ID:'+str(data['userData']['plateId']))
    print('背景ID:'+str(data['userData']['frameId']))
    print('称号ID:'+str(data['userData']['titleId']))
    print('搭档ID:'+str(data['userData']['partnerId']))
    #旅行伙伴
    id=0
    for a in range(5):#所有旅行伙伴
        print('旅行伙伴'+str(id+1)+' ID:'+str(data['userData']['charaSlot'][id]))
        id=id+1
    #游玩次数
    print('游玩次数信息:')
    print('游玩总次数:'+str(data['userData']['playCount']))
    print('现游玩总次数:'+str(data['userData']['currentPlayCount']))
    print('总DX分数:'+str(data['userData']['totalDeluxscore']))
    #游玩版本、日期
    print('游玩版本、日期信息:')
    print('最后游玩版本:'+str(data['userData']['lastRomVersion']))
    print('最后游玩数据版本:'+str(data['userData']['lastDataVersion']))
    print('最后登录时间:'+str(data['userData']['lastLoginDate']))
    print('最后游玩时间:'+str(data['userData']['lastPlayDate']))
    print('最后游玩地区:'+str(data['userData']['lastRegionName']))
    print('最后游玩地区ID:'+str(data['userData']['lastRegionId']))
    print('首次游玩版本:'+str(data['userData']['firstRomVersion']))
    print('首次游玩版本:'+str(data['userData']['firstDataVersion']))
    print('首次游玩时间:'+str(data['userData']['firstPlayDate']))

def ticket(token,qrcode,chargeId=2):
    token={
        "Authorization":'Bearer '+token
    }
    if chargeId==2 or chargeId==3 or chargeId==5:
        payload={
            "qrcode":qrcode,
            "chargeId":chargeId,
        }
    else:
        print('参数chargeId仅允许 2/3/5:2倍票/3倍票/5倍票')
        return
    data=post('https://api.wmc.pub/v1/charge',headers=token,json=payload)
    print(data)

def updatelx(token,qrcode,key):
    token={
        "Authorization":'Bearer '+token
    }
    payload={
        "qrcode":qrcode,
        "key":key,
    }
    data=post('https://api.wmc.pub/v1/update-lx',headers=token,json=payload)
    print(data)

def maiulx(token,qrcode,key):
    token={
        "Authorization":'Bearer '+token
    }
    payload={
        "qrcode":qrcode,
        "key":key,
    }
    data=post('https://api.wmc.pub/v1/update-lx',headers=token,json=payload)
    print(data)

def updatefish(token,qrcode,key):
    token={
        "Authorization":'Bearer '+token
    }
    payload={
        "qrcode":qrcode,
        "token":key,
    }
    data=post('https://api.wmc.pub/v1/update-lx',headers=token,json=payload)
    print(data)

def maiu(token,qrcode,key):
    token={
        "Authorization":'Bearer '+token
    }
    payload={
        "qrcode":qrcode,
        "token":key,
    }
    data=post('https://api.wmc.pub/v1/update-lx',headers=token,json=payload)
    print(data)