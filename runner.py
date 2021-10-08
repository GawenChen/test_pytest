# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/8 16:02
@Auth ： 潇湘
@File ：runner.py
@IDE ：PyCharm
@QQ : 810400085
"""
import os

import pytest

# pytest.main(['-s','EDC_Suites/test_login.py','--alluredir','./temp'])
# os.system('allure generate ./temp -o./allure-report --clean')

pytest.main(['-s','Web/example3.py'])