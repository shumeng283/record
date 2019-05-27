# Author :lixinhao
from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/yoyoketang/")
driver.implicitly_wait(5)
page = driver.page_source
url_list = re.findall('href=\"(.*?)\"',page,re.S)
url_all = []
for url in url_list:
    if "http" in url:
        url_all.append(url)
print(url_all)