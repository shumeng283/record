import requests
import datetime

url_list = {'https://jdb.hffss.com/ManagersDetails?corpid=100003150',
            'https://jdb.hffss.com/FutuBaseList?corpid=200000078'}

error_url = []
def test_url():
    for url in url_list:
        re = requests.get(url)
        code = re.status_code
        if code == 200:
            # 获取当前时间
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(nowTime, url, code)
            error_url.append(url)
        else:
            pass

test_url()