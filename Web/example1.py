import time

from selenium  import webdriver


# 打开浏览器
driver = webdriver.Chrome()

# 打开网站
driver.get("http://localhost/mgr/login/login.html")

# 找到用户输入框
# driver.find_element_by_xpath('//*[@id="username"]').send_keys('auto')
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('sdfsdfsdf')
driver.find_element_by_xpath('//*[@id="login-page"]').click()
#操作元素
# time.sleep(5)
# driver.close()


# C:\Users\ChenGen\AppData\Local\Google\Chrome\Application