# -*- coding: utf-8 -*-
'''
@File    :   get_token.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/5/11 9:30  
'''


class Get_Token:
    access_token = None


setattr(Get_Token, 'access_token', '111')
print(getattr(Get_Token,'access_token'))
