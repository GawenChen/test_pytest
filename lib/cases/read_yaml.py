# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 17:43
@Auth ： 潇湘
@File ：read_yaml.py
@IDE ：PyCharm
@QQ : 810400085
"""
import yaml

with open('./edc_login.yaml', encoding='utf8') as f:
    datas = yaml.safe_load(f)

datas = datas['loginPage'][0]
testcases = datas['cases']
for cases in testcases:
    listcase = list(cases.values())
    print(listcase)