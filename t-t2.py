# Author :lixinhao
import time
dict = {'user':None,'status':False}
'''
def timer(func):
    def inner(*args,**kwargs):
        if dict['user'] and dict['status']:
            print('已登录！')
            res = func(*args,**kwargs)
            return res
        name = input('>>:').strip()
        pwd = input('>>:').strip()
        if name == 'sm' and pwd == '123':
            print('登录成功')
            dict['user'] = 'sm'
            dict['status'] = True
            res = func(*args, **kwargs)
            return res
    return inner

@timer
def index():
    time.sleep(1)
    print('欢迎index')
    return '返回index'

@timer
def home(name):
    time.sleep(1)
    print('欢迎home【%s】' %name)
    return '返回home'

print(index())
print(home('sm'))
'''
def timer(func):
    def inner(*args,**kwargs):
        if dict['user'] and dict['status']:
            print('已登录')
            res = func(*args,**kwargs)
            return res
        name = input('>>:').strip()
        pwd = input('>>:').strip()
        if name == 'sm' and pwd == '123':
            print('登录成功')
            dict['user'] = 'sm'
            dict['status'] = True
            res = func(*args, **kwargs)
            return res
    return inner

@timer
def index():
    time.sleep(1)
    print('hello')
    return 'hahahah'

@timer
def home():
    time.sleep(2)
    print('hello2')
    return 'hehehehe'

print(index())
print(home())