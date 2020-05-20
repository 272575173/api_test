# -*- coding: utf-8 -*-
'''
@File    :   read_config.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/5/11 16:59  
'''

import configparser

class ReadConfig:
    def get_config(self,file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]


if __name__ == '__main__':
    from tools import project_path
    print(ReadConfig().get_config(project_path.case_config_path,'MODE','mode'))