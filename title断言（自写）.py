# Author :lixinhao
from selenium import webdriver
import time

def search(writ):
    driver.find_element_by_xpath("//input[@id='kw']").send_keys(writ)
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='kw']").submit()
    time.sleep(2)
    driver.find_element_by_xpath("//h3[@class='t c-gap-bottom-small']/a").click()
    time.sleep(5)

def tab(ttt):
    handle = driver.window_handles
    driver.switch_to.window(handle[1])
    title = driver.title
    if title == ttt:
        print("true")
    else:
        print('false,title错误')

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com/")
    driver.implicitly_wait(5)
    search('哈哈')
    tab('哈哈（汉字词语）_百度百科')