# Author :lixinhao
import random,hashlib
from datetime import *

print(random.random())
print(random.randint(1,19))
print(random.randrange(1,19,2))
print(random.randint(13000000000,13999999999))

y = date.today()
print(y)

now = datetime.today()
now_y = now.year
next_week = now + timedelta(days=7)
tomorrow = now + timedelta(days=1)
next_week_hour = now + timedelta(hours=1)
print(now_y)
print(next_week)
print(next_week_hour)

md5 = hashlib.md5(b'12345')
pass_word = md5.hexdigest()
print(pass_word)


file = open('C://Users/lixh/Desktop/21.txt',mode="a+")
file.write('sss'+'\n')
file.write('yyy'+'\n')
res = file.readlines()
for i in res:
    print(i)
file.close()
