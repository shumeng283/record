import random
from functools import reduce
a = reduce(lambda x,y:x*y,[1,2,3,4])
print(a)

def dg(x):
    if x == 1:
        return 1
    else:
        return x * dg(x-1)
print(dg(5))

aa = 0
bb = 1
xx = []
while bb < 100:
    aa,bb = bb,aa+bb
    xx.append(aa)
print(xx)

def mi(x,n):
    if x == 0:
        return 1
    else:
        return n * (mi(x-1,n))
print(mi(3,4))

