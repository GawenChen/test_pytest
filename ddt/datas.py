# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 17:52
@Auth ： 潇湘
@File ：datas.py
@IDE ：PyCharm
@QQ : 810400085
"""

import yaml

datas = None

with open('./lib/cases/edc_login.yaml', encoding='utf8') as f:
    datas = yaml.safe_load(f)

