# coding:utf-8
import json
import requests
import unittest
import HTMLTestRunner

class crop(unittest.TestCase):
    '''私募管理人'''
    def setUP(self):
        pass
    def test_search(self):
        '''搜索类型'''
        url = 'https://api.jdb.hffss.com//attent/corpids/list'
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Content-Type": "application/json, text/plain, */*",
            "Host": "api.jdb.hffss.com",
            "oid": "obgs71WOxNmem_hMWqxBWwOtEstc",
            "Origin": "http://jdb.hffss.com",
            "rb": "",
            "Referer": "http://jdbtest.hffss.com/ManageAgency",
            "sid": "031b3ea8037f3e86",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) \
            AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 \
            wechatdevtools/1.02.1901230 MicroMessenger/6.7.3 Language/zh_CN \
            webview/15561554780482248 webdebugger port/55904"
        }
        r = requests.post(
            url=url,
            headers=headers,
            data=json.dumps({}))
        print(r.text)
        print(r.status_code)
        self.assertEqual(
            r.json()['status'], 'success')

    def test_hot(self):
        '''热门搜索'''
        url = 'https://api.jdb.hffss.com/corp/orghotwords'
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Content-Type": "application/json;charset=utf-8",
            "Host": "api.jdb.hffss.com",
            "oid": "obgs71WOxNmem_hMWqxBWwOtEstc",
            "Origin": "https://jdb.hffss.com",
            "rb": "",
            "Referer": "https://jdb.hffss.com/ManageAgency",
            "sid": "031b3ea8037f3e86",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) \
            AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 \
            wechatdevtools/1.02.1901230 MicroMessenger/6.7.3 Language/zh_CN \
            webview/15561554780482248 webdebugger port/55904",
        }
        r = requests.post(
            url=url,
            data=json.dumps({}),
            headers=headers)
        print(r.text)
        print(r.status_code)
        self.assertEqual(
            r.json()['status'], 'success')

def suite():
    loginTestCase = unittest.makeSuite(crop, "test")
    return loginTestCase

if __name__ == '__main__':
    fr = open("res3.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title="接口测试报告",description="测试用例结果",tester=u"舒萌")
    runner.run(suite())
    fr.close()
