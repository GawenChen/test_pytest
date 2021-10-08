from selenium import webdriver


class Comm:
    """
    电商项目PO封装
    """

    def __init__(self):
        """
        构造函数，创建对象的时候会执行
        """
        self.driver = webdriver.Chrome()

    def Login(self):
        self.driver.get("http://localhost/mgr/login/login.html")

        # 找到用户输入框
        # driver.find_element_by_xpath('//*[@id="username"]').send_keys('auto')
        # driver.find_element_by_xpath('//*[@id="password"]').send_keys('sdfsdfsdf')
        self.driver.find_element_by_xpath('//*[@id="login-page"]').click()


if __name__ == '__main__':
    comm = Comm()
    comm.Login()
