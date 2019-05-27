# Author :lixinhao
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(5)
def is_exist(x_path):
    s = driver.find_elements_by_xpath(xpath=x_path)
    if len(s) == 0:
        print("元素未找到：%s" % x_path)
    elif len(s) == 1:
        print("true")
        return True
    else:
        print("找到%s个元素：%s" % (len(s), x_path))
        return False

#if is_exist("//input[@id='kw']"):
#    driver.find_element_by_id("kw").send_keys('sb')
if is_exist("//span/input"):
    driver.switch_to.frame("form")
    print('ok')
    driver.find_element_by_tag_name("input").send_keys("yoyoketang")