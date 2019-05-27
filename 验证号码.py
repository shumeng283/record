# Author :lixinhao

def number_test():
    while True:
        number = input('请输入电话号码：')
        CN_mobile = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
        CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
        CN_telecom = [133, 153, 180, 181, 189, 177, 1700]
        number_3 = int(number[0:3])
        number_4 = int(number[0:4])
        if len(number) == 11:
            if number_3 in CN_mobile or number_4 in CN_mobile:
                print('移动号码')
                print('号码为：{}'.format(number))
                break
            elif number_3 in CN_telecom or number_4 in CN_telecom:
                print('电信号码')
                print('号码为：{}'.format(number))
                break
            elif number_3 in CN_union or number_4 in CN_union:
                print('联通号码')
                print('号码为：{}'.format(number))
                break
            else:
                print('号码错误，请重新输入')
        else:
            print('位数不对，请重新输入')
number_test()