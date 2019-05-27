# Author :lixinhao
import requests,unittest,HTMLTestRunner,json

class crop(unittest.TestCase):
    '''私募管理人'''
    def setUP(self):
        pass
    def test_search(self):
        '''搜索类型'''
        self.url = 'https://api.jdb.hffss.com//attent/corpids/list'
        headers = {
            "Accept":"application/json, text/plain, */*",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Content-Type":"application/json;charset=utf-8",
            "Host":"api.jdbtest.hffss.com",
            "oid":"os7b1vx_f2NO9vM0ItahTab2oPgA",
            "Origin":"http://jdbtest.hffss.com",
            "Proxy-Connection":"keep-alive",
            "rb":"",
            "Referer":"http://jdbtest.hffss.com/ManageAgency",
            "sid":"27a809f70169ea17",
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 wechatdevtools/1.02.1901230 MicroMessenger/6.7.3 Language/zh_CN webview/15561554780482248 webdebugger port/55904"
        }
        r = requests.post(url=self.url,headers=headers)
        print(r.text)
        print(r.status_code)
        self.assertEqual(r.json(),'{"data":{"attentCorpids":[100003150,100000492,100000490,100000229,100000837,100001774,100000193,100000126,100003265,100001705]},"status":"success"}')
    def test_hot(self):
        '''热门搜索'''
        self.url = 'https://api.jdb.hffss.com/corp/orghotwords'
        form = {
            'Origin': 'https: // jdb.hffss.com',
            'Referer': 'https: // jdb.hffss.com / ManageAgency'
        }
        r = requests.post(url=self.url,data=form)
        print(r.text)
        print(r.status_code)
        self.assertEqual(r.json(),'{"data":{"orghots":[{"id":100003150,"name":"恒天中岩投资管理有限公司","type":1,"stockcode":null},{"id":100011896,"name":"厦门坚果兄弟投资管理有限公司","type":1,"stockcode":null},{"id":400000018,"name":"招商财富资产管理有限公司","type":4,"stockcode":null},{"id":400000030,"name":"深圳市融通资本管理股份有限公司","type":4,"stockcode":null},{"id":200000078,"name":"永安期货股份有限公司","type":2,"stockcode":null},{"id":200000062,"name":"创元期货股份有限公司","type":2,"stockcode":null},{"id":700000001,"name":"国泰基金管理有限公司","type":7,"stockcode":null},{"id":700000088,"name":"国寿安保基金管理有限公司","type":7,"stockcode":null},{"id":300000104,"name":"广发证券股份有限公司","type":3,"stockcode":null},{"id":300000087,"name":"华西证券股份有限公司","type":3,"stockcode":null},{"id":500000004,"name":"中粮信托有限责任公司","type":5,"stockcode":null},{"id":500000037,"name":"安徽国元信托有限责任公司","type":5,"stockcode":null}]},"status":"success"}')

def suite():
    loginTestCase = unittest.makeSuite(crop,"test")
    return loginTestCase

if __name__ == '__main__':
    fr = open("res3.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title='尽调宝接口测试',description='测试用例结果',tester='舒萌')
    runner.run(suite())
