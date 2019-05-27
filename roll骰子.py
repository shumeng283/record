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
    print('<<<游戏开始！>>>')
    c = ['大','小']
    input_c = input('请输入大或小：')
    if input_c in c:
        tt = sum(roll_s())
        win = input_c == roll_b(tt)
        if win:
            print('分数：',tt,'你赢了')
        else:
            print('分数：',tt,'你输了')
    else:
        print('不符合条件，重新输入')
        game_s()
game_s()