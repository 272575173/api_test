# -*- coding: utf-8 -*-
'''
@File    :   .py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/3/6 10:28 
'''
import unittest
from config.tools import read_yaml,write_yaml,read_yaml_extract
from config.logger_info import logger
from wu_sendres.http_request_01 import Http_Client
from ddt import ddt, unpack, file_data, data
import time
from HTMLTestRunner import HTMLTestRunner
from wu_requests.get_datas import Get_Data
@ddt
class Api_TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.Http_Client = Http_Client()
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def assert_res(self,expect, actual):
        for key, value in expect.items():  #循环预期结果 做判断
            if key in actual:  #如果预期的key 在实际结果key里面
                self.assertEqual(value, actual[key])  #判断预期的值与实际值是否相等
                logger.info('api--ok')
            else:
                for _key, _value in actual.items():         #循环实际结果
                    if isinstance(_value,dict) and (key in _value): #实际结果值如果是字典且key在实际结果里面
                        self.assertEqual(value,_value[key])
                        expect_new={}
                        expect_new[key]=value
                        self.assert_res(expect_new,_value)
                        logger.info('api dict--ok')


    # @data(*case_info)
    @file_data(r'../config/cases_data.yaml')
    def test01_login(self,**data):
        res_login = self.Http_Client.send_requests(data['method'], name=data['api_name'], data=data['data'])
        # setattr(res_login,'token',res_login['data']['access_token'])
        # print(setattr(res_login,'token',res_login['data']['access_token']))
        # print(getattr('1111111111111111',res_login,'token'))
        if res_login['data']['access_token']:
            setattr(Get_Data,'accesstoken',res_login['data']['access_token'])
        var_data = data['assert']
        self.assert_res(var_data,res_login,)

if __name__ == '__main__':
    # unittest.main()
    tesecase=unittest.TestSuite()
    tesecase.addTest(unittest.TestLoader().loadTestsFromTestCase(Api_TestCase))
    dir =r'E:\wu_pytest\wu_requests\report\test3.html'
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    file=open(dir,'wb')
    runner=HTMLTestRunner(stream=file,title='接口测试报告',description='结果',)
    runner.run(tesecase)
    file.close()


