# Author :lixinhao
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys('测试部落')
driver.find_element_by_id("kw").submit()
s = driver.find_elements_by_xpath("//h3[@class='t']/a")
time.sleep(3)
s[0].click()
driver.implicitly_wait(10)
handles = driver.window_handles
driver.switch_to.window(handles[1])
driver.find_element_by_id("btn_search").click()
driver.find_element_by_id("txt_search").clear()
driver.find_element_by_id("txt_search").send_keys("selenium")
driver.find_element_by_id("txt_search").submit()
time.sleep(3)
driver.quit()