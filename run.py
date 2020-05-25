# -*- coding: utf-8 -*-
'''
@File    :   run.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/5/11 9:28  
'''
import unittest,time
from tools.http_request import HttpRequst
from tools.read_write_excel import Open_Excel
from ddt import ddt,data
from HTMLTestRunner import HTMLTestRunner
from tools.logger_info import logger
from tools.project_path import *


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
        self.assertEqual(datas['assert'],res['code'])

if __name__ == '__main__':
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Cases))
    # now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    # file=open(test_report_path,'wb')
    # runner=HTMLTestRunner(stream=file,title='接口测试报告',description='结果',)
    # runner.run(suite)
    # file.close()
