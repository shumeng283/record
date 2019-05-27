# Author :lixinhao
l = []
for i in range(100,1000):
    s = 0
    m = list(str(i))
    for j in m:
        s += int(j) ** 3
    if s == i:
        l.append(i)
print(l)

ll = []
for i in range(1,1000):
    s = 0
    for j in range(1,i):
        if i % j == 0 and i > j:
            s += j
    if s == i:
        ll.append(i)
print(ll)
