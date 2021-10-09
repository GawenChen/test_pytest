# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 16:17
@Auth ： 潇湘
@File ：webkeys.py
@IDE ：PyCharm
@QQ : 810400085
"""
from selenium import webdriver


class WebKey:
    def __init__(self):
        self.driver = None

    def openbrowser(self, browser= 'gc'):
        """
        :param br:gc=谷歌浏览器；ff=火狐；ie=IE
        :return:
        """
        if browser == 'gc':
            self.driver = webdriver.Chrome()
        elif browser == 'ff':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            print("浏览器不支持！请在此添加代码实现")
        # 隐式等待默认10秒
        self.driver.implicitly_wait(10)

    def geturl(self, url=None):
        self.driver.get(url)

    def __find__ele(self, locator=''):
        """
        支持八种定位方式
        :param self:
        :param locator:xpath=//*[@id="username"]
        :return: 放回定位到的元素
        """
        ele = None
        self.ele = None
        if locator.startswith('xpath='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=') + 1:])
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(
                locator[locator.find('=') + 1:])
        elif locator.startswith('name='):
            ele = self.driver.find_element_by_name(
                locator[locator.find('=') + 1:])
        elif locator.startswith('tag_name='):
            ele = self.driver.find_element_by_tag_name(
                locator[locator.find('=') + 1:])
        elif locator.startswith('link_text='):
            ele = self.driver.find_element_by_link_text(
                locator[locator.find('=') + 1:])
        elif locator.startswith('partial_link_text='):
            ele = self.driver.find_element_by_partial_link_text(
                locator[locator.find('=') + 1:])
        elif locator.startswith('css_selector='):
            ele = self.driver.find_element_by_css_selector(
                locator[locator.find('=') + 1:])
        else:
            ele = self.driver.find_element_by_xpath(locator)

        self.ele = ele
        return ele

    def click(self, locator=None):
        """
        找到，并点击元素
        :param locator:定位器，默认xpath
        :return:
        """
        ele = self.__find__ele(locator)
        ele.click()

    def input(self, locator=None, value=None):
        """
        找到元素，并完成封装
        :param locator: 定位器，默认xpath
        :param value: 需要输入的字符串
        :return:
        """
        ele = self.__find__ele(locator)
        ele.send_keys(str(value))

    def intoiframe(self, locator=None):
        """
        进入frame
        :param locator:
        :return:
        """
        ele = self.__find__ele(locator)
        self.driver.switch_to.frame(ele)

    def quit(self):
        """
        退出
        :return:
        """
        self.driver.quit()