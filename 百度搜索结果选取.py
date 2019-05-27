# Author :lixinhao
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com/")
driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys('博客')
driver.find_element_by_xpath("//input[@value='百度一下']").click()
time.sleep(1)
xx = driver.find_elements_by_xpath("//div[@srcid='1599']")
for x in xx:
    print(x.get_attribute('id'))
time.sleep(3)
if len(xx) > 1:
    xx[2].click()
    print(driver.current_url)
else:
    print("未获取")