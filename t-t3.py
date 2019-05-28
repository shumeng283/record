# Author :lixinhao
l = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
m = [i for i in l if i < 0]
n = [i for i in l if i > 0]
print('正数%s,负数%s' %(len(n),len(m)))

s = 'axbyczdj'
print(s[0::2])

ss = 'hello_world_yoyo'
print(ss.split('_'))

a = 1
print('%04d' %a)

aa = [1,3,5,7]
aa.insert(3,1)
print(aa[1:])