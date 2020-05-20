# -*- coding: utf-8 -*-
'''
@File    :   project_path.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/5/11 11:28  
'''

import os
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(project_path)

test__excel_path=os.path.join(project_path,'test_datas','test.xlsx')
print(test__excel_path)

test_report_path=os.path.join(project_path,'test_api_wu','report')

case_config_path=os.path.join(project_path,'config','case+config')

os.access(case_config_path,mode)