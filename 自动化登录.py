# Author :lixinhao
from selenium import webdriver
import time

def login(driver,user,password):
    driver.get("https://github.com/login")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//input[@id='login_field']").send_keys(user)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("commit").click()

def logout(driver):
    time.sleep(3)
    driver.find_element_by_xpath("//summary[@class='HeaderNavlink name mt-1']").click()
    time.sleep(1)
    t = driver.find_element_by_xpath("//li[@class='dropdown-header header-nav-current-user css-truncate']/strong").text
    print("获取到我的账户名称：{}".format('shumeng283'))
    if t == "shumeng283":
        print("登录成功！")
    else:
        print("登录失败！")
    driver.find_element_by_xpath("//button[@class='dropdown-item dropdown-signout']").click()
    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    driver = webdriver.Firefox()
    login(driver,'shumeng283','s123456')
    print('hello')
    logout(driver)
