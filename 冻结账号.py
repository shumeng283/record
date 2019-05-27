# Author :lixinhao

pass_list = ['**','12345']
def account_login():
    tries = 3
    while tries > 0 :
        password = input('请输入密码： ')
        if password == pass_list[-1]:
            print('输入正确')
            break
        elif password == pass_list[0]:
            pass_new = input('请输入新密码： ')
            pass_list.append(pass_new)
            print('密码已变更')
            account_login()
            break
        else:
            print('输入错误,请再输入一遍')
            tries = tries - 1
    else:
        print('被冻结')
account_login()