# Author :lixinhao

import  random
def roll_s(numbers = 3,s_list = None):
    print('<<<Roll大小>>>')
    if s_list is None:
        s_list = []
        while numbers > 0:
            s = random.randrange(1,7)
            s_list.append(s)
            numbers = numbers - 1
        return s_list

def roll_b(tt):
    big = 11 <= tt <= 18
    small = 3 <= tt <= 10
    if big:
        return '大'
    elif small:
        return '小'

def game_s():
    money = 1000
    while money > 0:
        print('<<<游戏开始！>>>')
        c = ['大', '小']
        input_c = input('请输入大或小：')
        if input_c in c:
            tt = sum(roll_s())
            win = input_c == roll_b(tt)
            money_c = int(input('请输入押注金额：'))
            if win:
                print('点数',tt,'你赢了')
                money = money + money_c
                print('剩余金额：{}'.format(money))
            else:
                print('点数',tt,'你输了')
                money = money - money_c
                print('剩余金额：{}'.format(money))
        else:
            print('不符合条件，重新输入')
    print('游戏结束')
game_s()