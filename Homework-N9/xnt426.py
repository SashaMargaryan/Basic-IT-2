import random

def func(n,a=-5,b=20):
    ar=[]
    for i in range(n):
        ar.append(random.randint(a,b))
    return ar
a2=[]

s=4
for i in range(s):
    a2.append(func(s))
for i in a2:
    print(i)

d = 0
n=len(a2)
for i in range(0,n-1):
    for j in range( 0,n-1-i):

        if a2[i][j]%2 == 0:
            d = d + 1
        print(a2[i][j], end=' ')
    print()
print(d)
