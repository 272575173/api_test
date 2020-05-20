# -*- coding: utf-8 -*-
'''
@File    :   .py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/3/6 10:28 
'''
import yaml,os
import logging
import unittest
from ruamel import  yaml

yaml_path=os.path.abspath(os.path.dirname(__file__))
test_data_path= yaml_path+'/test_data.yaml'
extract_path=yaml_path+'/extract.yaml'
test_path=yaml_path+'111.yaml'
def read_yaml():
    with open(test_data_path,'r',encoding='utf8') as f:
        cfg=yaml.load(f.read())
    return cfg

def write_yaml(extract_dict):
    with open(extract_path,'w') as f:
        yaml.dump(extract_dict,f)


def read_yaml_extract():
    with open(extract_path,'r',encoding='utf-8') as f:
        token=yaml.load(f.read())
    return token
# def write_yaml(extract_dict):
#     with open(current_path+'\config\extract.yaml','w') as f:
#         yaml.dump(extract_dict, f, Dumper=yaml.RoundTripDumper)
#
# def read_yaml():
#     with open(config_path,'r',encoding='utf-8') as f:
#         cfg=yaml.load(f,Loader=yaml.RoundTripLoader,preserve_quotes=True)
#         #print(type(cfg),cfg)
#         return cfg
#
# def read_yaml_extract(data):
#     with open(current_path+'\config\extract.yaml','r',encoding='utf-8') as f:
#         cfg=yaml.load(f,Loader=yaml.RoundTripLoader,preserve_quotes=True)
#         data=cfg[data]
#         #print(type(cfg),cfg)
#         return data

# def get_path(new_path):
#     for path in os.listdir(new_path):
#         if os.path.isdir(path):
#             os.listdir(os.path.join(os.getcwd(),path))
#             print('还要处理一下',os.path.join(os.getcwd(),path))
#         else:
#             print('没了',os.path.join(os.getcwd(),path))

# def write_yaml_extract(extract_data):
#     with open(test_path,'w') as f:
#         for k,v in extract_data.items():
#             if 'extract' in extract_data:
#









































# def write_yaml(extract_dict):
#     with open(test_data_path,'w') as f:
#         yaml.dump(extract_dict, f, Dumper=yaml.RoundTripDumper)
#
# def read_yaml():
#     with open(test_data_path,'r',encoding='utf-8') as f:
#         cfg=yaml.load(f,Loader=yaml.RoundTripLoader,preserve_quotes=True)
#         #print(type(cfg),cfg)
#         return cfg
#
# def read_yaml_extract(data):
#     with open(test_data_path,'r',encoding='utf-8') as f:
#         cfg=yaml.load(f,Loader=yaml.RoundTripLoader,preserve_quotes=True)
#         data=cfg[data]
#         #print(type(cfg),cfg)
#         return data
#
