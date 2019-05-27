# Author :lixinhao
dict ={
    'sm1':{'pwd':'123','count':0},
    'sm2':{'pwd':'123','count':0},
    'sm3':{'pwd':'123','count':0}
}

while count < 3:
    name = input('>>:').strip()
    if  not name:
        print('用户名为空，请重新输入')
        continue
    elif name not in dict:
        print('用户名错误，请重新输入')
        continue
    if name in dict:
        print('用户名正确')
    with open('C:/Users/lixh/Desktop/1.txt','r') as f:
        rf = f.read().split('|')
        if dict[name] in rf:
            print('【%s】被锁定' %s)
            f.close()
            break
    if dict[name]['count'] == 3:
        print('账号锁定！')
        with open('C:/Users/lixh/Desktop/1.txt','a') as f:
            f.write('%s|' %name)
            f.close()
    pwd = input('>>:').strip()
    if pwd == dict[name]['pwd']:
        print('登录成功！')
        break
    else:
        print('错误！！！')
        dict[name]['count'] += 1
