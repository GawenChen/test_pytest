# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/8 16:03
@Auth ： 潇湘
@File ：test_login.py
@IDE ：PyCharm
@QQ : 810400085
"""
import pytest
from ddt.datas import datas
from EDC_Suites.webkeys import WebKey


class Test_Edc:
    """
    EDC项目PO封装
    """
    def setup_class(self):
        """
        构造函数
        :return:
        """
        self.web = WebKey()
        self.web.openbrowser()

    @pytest.mark.parametrize('listcases', datas['loginPage'])
    def test_login(self, listcases):
        # self.web.geturl("https://demodata.liangyihui.net/newlogin.html")
        # self.web.input('*//div/input[@id="login_account"]', 18616269204)
        # self.web.input('//div/input[@id="login_password"]', '123456a')
        # self.web.click('//span[text()="登录"]')

        testcases = listcases['cases']
        for cases in testcases:
            # func = getattr(self.web, cases[0])  # cases得到的是一个字典
            listcase = list(cases.values())
            func = getattr(self.web, listcase[1])
            values = listcase[2:]
            func(*values)

    def teardown_class(self):
        self.web.quit()

