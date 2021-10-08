# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/8 17:57
@Auth ： 潇湘
@File ：example3.py
@IDE ：PyCharm
@QQ : 810400085
"""
import pytest


def sum(x,y):
    return x+y

class Test_Data:

    @pytest.mark.parametrize("x,y,z", [
                            [1, 2, 3],
                            [2, 3, 5],
    ])
    def test_sum(self, x, y, z):
        """
        测试相加
        :return:
        """
        assert sum(x, y) == z