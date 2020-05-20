# -*- coding: utf-8 -*-
'''
@File    :   .py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/3/6 10:28 
'''
import logging



logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
fmt = logging.Formatter('[%(filename)-6s]:[%(levelname)-6s][%(asctime)s]:%(message)s')
stram_hd1 = logging.StreamHandler()
stram_hd1.setFormatter(fmt)
stram_hd1.setLevel(logging.DEBUG)
logger.addHandler(stram_hd1)
