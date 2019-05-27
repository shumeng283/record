# Author :lixinhao

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(15)
s = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(s).perform()
driver.find_element_by_link_text("搜索设置").click()
b = driver.find_element_by_xpath("//select[@id='nr']")
Select(b).select_by_index(2)
time.sleep(2)
driver.find_element_by_link_text("保存设置").click()
time.sleep(3)
d = driver.switch_to.alert
print(d.text)
d.dismiss()
