# -*- coding: utf-8 -*-
'''
@File    :   http_request.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/5/9 10:41  
'''

import requests
from tools.read_write_excel import Open_Excel
import json
from tools.logger_info import logger


class HttpRequst:

    def http_request(self, method, url, data, headers=None, access_token=None):
        if access_token:
            for k, v in access_token.items():
                headers['accesstoken'] = v
        if method.upper() == 'GET':
            try:
                res = requests.get(url=url, data=data, headers=headers).json()
            except Exception as e:
                raise print('get接口错误', e)

        elif method.upper() == 'POST':
            res = requests.post(url=url, data=data, headers=headers).json()
        else:
            print('输入正确请求方法')
        return res
# if __name__ == '__main__':
#     test_datas=().get_testdatas(r'C:\Users\Administrator\Desktop\test.xlsx','case')
#     for value_data in  test_datas:
#         result=HttpRequst().http_request(value_data['method'],value_data['url'],eval(value_data['data']),eval(value_data['headers']))
#         # logger.info(result)
#         # assert result['code']==eval(value_data['assert'])['code']
#         print(result['code'],type(result['code']))
#         print(eval(value_data['assert'])['code'])
#
