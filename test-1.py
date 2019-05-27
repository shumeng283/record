# Author :lixinhao
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(15)
driver.find_element_by_css_selector("#kw").send_keys("测试部落")
driver.find_element_by_css_selector("#kw").submit()
s = driver.find_elements_by_css_selector("h3.t>a")
for i in s:
    print(i.get_attribute("href"))