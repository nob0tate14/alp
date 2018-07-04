'''
Created on 2018/07/04

@author: u18user
'''
from os.path import dirname, abspath


ALP_DIR = dirname(dirname(abspath(__file__)))
print(__file__)
print(abspath(__file__))
print(dirname(__file__))

BAT_DIR = f"{ALP_DIR}/resource/bat"

CONF_DIR = f"{ALP_DIR}/resource/conf"
