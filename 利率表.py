# Author :lixinhao

def invest(amount,rate,time):
    print('资金：{}' .format(amount))
    for t in range(1,1+time):
        amount = amount * (1 + rate)
        print('第{}年：${}' .format(t,amount))
invest(999,0.2,6)