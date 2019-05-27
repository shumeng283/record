# coding:utf-8
# Author :lixinhao

import json

import requests
import unittest
import HTMLTestRunner




class crop(unittest.TestCase):
    '''私募管理人'''

    url = 'http://api.jdbtest.hffss.com//attent/corpids/list'

    def setUP(self):
        pass

    @property
    def headers(self):
        return {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Content-Type": "application/json, text/plain, */*",
            "Host": "api.jdbtest.hffss.com",
            "oid": "os7b1vx_f2NO9vM0ItahTab2oPgA",
            "Origin": "http://jdbtest.hffss.com",
            # "Proxy-Connection": "keep-alive",
            "rb": "",
            "Referer": "http://jdbtest.hffss.com/ManageAgency",
            "sid": "27a809f70169ea17",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) \
AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 \
wechatdevtools/1.02.1901230 MicroMessenger/6.7.3 Language/zh_CN \
webview/15561554780482248 webdebugger port/55904"
        }

    def test_search(self):
        '''搜索类型'''
        r = requests.post(
            self.url,
            headers=self.headers,
            data=json.dumps({}))
        print(r.text)
        print(r.status_code)
        self.assertEqual(
            r.json()['status'], 'success')

    # def test_hot(self):
    #     '''热门搜索'''
    #     self.url = 'http://api.jdb.hffss.com/corp/orghotwords'
    #     form = {
    #         'Origin': 'http: // jdb.hffss.com',
    #         'Referer': 'http: // jdb.hffss.com / ManageAgency'
    #     }
    #     r = requests.post(url=self.url, data=form, headers=self.headers)
    #     print(r.text)
    #     print(r.status_code)
    #     self.assertEqual(
    #         r.json()['status'], 'success')


def suite():
    loginTestCase = unittest.makeSuite(crop, "test")
    return loginTestCase


if __name__ == '__main__':
    fr = open("res3.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner('res3.html', stream=fr)
    runner.run(suite())
    fr.close()
