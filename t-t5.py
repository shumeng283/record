# Author :lixinhao

msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}

list = []
while True:
    for i in msg_dic:
        print(i,msg_dic[i])
        continue
    choice = input('请输入购买商品：').strip()
    if choice not in msg_dic:
        break
    count = input('请输入购买个数：').strip()
    if not count.isdigit():
        break
    list.append((choice,msg_dic[choice],count))
    print('商品{sp},价格{jg},数量{sl}' .format(sp=choice,jg=msg_dic[choice],sl=count))
