# Author :lixinhao
import unittest,requests
import HTMLTestRunner

class logintest(unittest.TestCase):
    """登录测试"""
    def setUp(self):
        self.url = "http://jira.hffss.com:8080/login.jsp"
    def testlogin1(self):
        """正确名字"""
        form = {"os_username":"shumeng","os_password":"s123456"}
        r = requests.post(self.url,headers=form)
        print(r.status_code)
        self.assertEqual(r.status_code,200)
    def testlogin2(self):
        """错误名字"""
        form = {"os_username":"","os_password":"s123456"}
        r = requests.post(self.url,headers=form)
        self.assertTrue(r.text,"对不起,你的用户名或者密码不正确 - 请重试。")
    def testlogin3(self):
        """错误密码"""
        form = {"os_username":"","os_password":""}
        r = requests.post(self.url,headers=form)
        self.assertTrue(r.text, "对不起,你的用户名或者密码不正确 - 请重试。")

def suite():
    loginTestCase = unittest.makeSuite(logintest,"test")
    return loginTestCase

if __name__ == '__main__':
    fr = open("res2.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title="接口测试报告",description="测试用例结果",tester=u"舒萌")
    runner.run(suite())