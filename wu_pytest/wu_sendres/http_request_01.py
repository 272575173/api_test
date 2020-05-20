# -*- coding: utf-8 -*-
'''
@File    :   .py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/3/6 10:28 
'''
import requests
import logging,json
from config.tools import read_yaml
from  config.logger_info import logger


# logger = logging.getLogger('test')
# logger.setLevel(logging.DEBUG)
# fmt = logging.Formatter('[%(filename)-6s]:[%(levelname)-6s][%(asctime)s]:%(message)s')
# stram_hd1 = logging.StreamHandler()
# stram_hd1.setFormatter(fmt)
# stram_hd1.setLevel(logging.DEBUG)
# logger.addHandler(stram_hd1)

api_data = read_yaml()  # 读取yaml文件数据
class Http_Client():
    INDEX=0
    def __init__(self):
        self.init_url_headers()

    def init_url_headers(self):
        self.url = api_data['api_url']
        self.headers = {
            'authorization': '9635969278{|}dac1c77942103b83fd7946ae28172978',
            'langue': 'en'
        }
    def get(self,data,headers):
        try:
            result=requests.get(url=self.url,params=data,headers=self.headers)
            return result.json()
        except BaseException as e:
            raise ('get接口错误',e)

    def post(self,data,headers):
        try:
            result=requests.post(url=self.url,data=data,headers=self.headers)
            return result.json()
        except BaseException as e:
            raise ('post接口错误',e)
    def send_requests(self,method,name=None,data=None,headers=None,files=None):
        Http_Client.INDEX+=1
        if headers:
            for key,value in headers.items():
                self.headers[key]=value
        # if data:
        #     if isinstance(data,dict):
        #         data=json.dumps(data) #字典转换为json串
        method=method.upper() # 大写接口方法名称
        res=''
        self.url=self.url+name  # 拼接URL
        if method=='GET':
            res=self.get(data,headers)
        elif method=='POST':
            res=self.post(data,headers)
        logger.info('第{3}次请求----接口地址{0},入参{1},请求头{2}'.format(self.url,data,self.headers,Http_Client.INDEX))
        logger.info('第{2}次请求返回----类型{0}，返回值：{1}'.format(type(res),res,Http_Client.INDEX))
        self.init_url_headers()
        return res