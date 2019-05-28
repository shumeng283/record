# Author :lixinhao
l = []
for i in range(100,1000):
    sum = 0
    m = list(str(i))
    for j in m:
        sum += int(j)**3
        if sum == i:
            l.append(i)
print(l)

ll = []
for i in range(1,1000):
    sum = 0
    for j in range(1,i):
        if i % j == 0 and i != j:
            sum += j
    if sum == i:
        ll.append(i)
print(ll)

a = [2,9,78,36,31,111,66]
b = range(1,len(a))[::-1]
for i in b:
    for j in range(i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    print('第%s冒泡,排序为%s' %(len(a)-i,a))