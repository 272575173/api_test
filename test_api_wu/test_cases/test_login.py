# -*- coding: utf-8 -*-
'''
@File    :   test_login.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/5/11 14:08  
'''

import unittest,time
from tools.http_request import HttpRequst
from tools.read_write_excel import Open_Excel
from ddt import ddt,data
from HTMLTestRunner import HTMLTestRunner
from tools.logger_info import logger
from tools.project_path import *
import json


test_data = Open_Excel().read_excel(test__excel_path, 'login')
@ddt
class Test_Cases(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*test_data)
    def test_login(self,datas):
        res=HttpRequst().http_request(method=datas['method'],url=datas['url'],data=eval(datas['data']),headers=eval(datas['headers']))
        logger.info('请求方法---{}-请求url---{}'.format(datas['method'],datas['url']))
        logger.info('请求头{}'.format(datas['headers']))
        logger.info('返回值{}--'.format(res))

        try:
            self.assertEqual(datas['assert'],res['code'])
            test_result='pass'
        except Exception as e:
            test_result = 'failed'
            raise e
        finally:
            Open_Excel().write_excel(test__excel_path, 'login', row=datas['id']+1,result=str(res),test_result=test_result)
if __name__ == '__main__':
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Cases))
    # now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    # file=open(test_report_path,'wb')
    # runner=HTMLTestRunner(stream=file,title='接口测试报告',description='结果',)
    # runner.run(suite)
    # file.close()
