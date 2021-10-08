from selenium import webdriver
from selenium.webdriver.common.by import By


class  EdcLogin:

    def __init__(self):
        self.driver = webdriver.Chrome()
        #隐式等待
        #每隔一秒钟找一次元素，如果超过等待的时间就会报没有找到元素
        self.driver.implicitly_wait(3)

    def edc_login(self):
        self.driver.get("https://demodata.liangyihui.net/newlogin.html")

        usename = self.driver.find_element(By.XPATH,'*//div/input[@id="login_account"]').send_keys(18616269204)
        userpwd = self.driver.find_element(By.XPATH,'//div/input[@id="login_password"]').send_keys('123456a')
        login = self.driver.find_element(By.XPATH,'//span[text()="登录"]').click()


    def enter_pro(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div').click()

if __name__ == '__main__':
        login = EdcLogin()
        login.edc_login()
        login.enter_pro()