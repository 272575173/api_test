# -*- coding: utf-8 -*-
'''
@File    :   Api_Auto_SendRequest.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/3/6 10:28 
'''

import requests
import json
# release 'Authorization': '9635969369{|}914cc2444e4f7ac666ebfcafa850f142'
#  test  authorization: 9635969278{|}dac1c77942103b83fd7946ae28172978
url_login='http://dev.dolphinco.net/offshore/login/index'

data={
    'account':'wu555',
    'password':'wu12345'
}
headers={
    #'Content-Type': 'application/x-www-form-urlencoded',
    'authorization': '9635969278{|}dac1c77942103b83fd7946ae28172978',
    'langue': 'en'
}
res_login=requests.post(url_login,data,headers=headers).json()
print(res_login)
print(res_login['data']['access_token'])
token=res_login['data']['access_token']


url_user='http://dev.dolphinco.net/offshore/user/index'
headers1={
    'accesstoken':token,
    'authorization': '9635969278{|}dac1c77942103b83fd7946ae28172978',
    'langue': 'en'
}
print(headers1['accesstoken'])
res_user=requests.request('get',url_user,headers=headers1).json()
result_user=json.dumps(res_user,sort_keys=True,indent=2)
print(res_user)
print(result_user)
