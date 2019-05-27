# Author :lixinhao

dic = {
    'u1':{'password':'123','count':0},
    'u2':{'password':'123','count':0},
    'u3':{'password':'123','count':0}
}

while True:
    name = input("请输入用户名：")
    if name not in dic:
        print('用户不存在')
        continue
    with open('C:/Users/lixh/Desktop/1.txt','r') as f:
        lock_users = f.read().split('|')
        if name in lock_users:
            print("该用户已锁定")
            break
    if dic[name]['count'] == 2:
        print('次数过多，被锁定')
        with open('C:/Users/lixh/Desktop/1.txt','a') as f:
            f.write('%s|' %name)
            continue
    password = input("请输入密码：")
    if password == dic[name]['password']:
        print('登录成功，欢迎')
        break
    else:
        print('用户名或密码错误')
        dic[name]['count'] += 1

