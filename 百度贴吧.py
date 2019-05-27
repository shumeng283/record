# Author :lixinhao

from selenium import webdriver
import time

def first(driver):
    driver.get("https://tieba.baidu.com/")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//a[@title='小小军团合战三国']").click()
    time.sleep(3)
    q = driver.window_handles
    driver.switch_to.window(q[1])

def second(driver,t1,t2):
    time.sleep(2)
    driver.find_element_by_xpath("//li[@class='tbui_aside_fbar_button tbui_fbar_post']/a").click()
    driver.find_element_by_xpath("//div[@class='j_title_wrap']/input").send_keys(t1)
    driver.find_element_by_xpath("//div[@class='edui-editor-middle']/div").send_keys(t2)

if __name__ == '__main__':
    profile = r'C:\Users\lixh\AppData\Roaming\Mozilla\Firefox\Profiles\hc7ljdnp.dev-edition-default'
    driver = webdriver.Firefox(profile)
    first(driver)
    print("OK")
    second(driver,"good","very good")