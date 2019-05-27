# Author :lixinhao

password_list = ['*#*','12345']
def account_login():
    password = input('请输入密码： ')
    if password == password_list[-1]:
        print('输入正确')
    elif password == password_list[0]:
        new_password = input('重置密码： ')
        password_list.append(new_password)
        print('密码已变更')
        account_login()
    else:
        print('输入错误')
        account_login()
account_login()