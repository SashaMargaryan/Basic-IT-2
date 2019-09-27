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

k = 2
d = 1

n=len(a2)
for i in range(0,n-1):
    for j in range(0,n-i):


        if a2[i][j]%k == 0:
            d = d * a2[i][j]

        print(a2[i][j], end=' ')

    print()

print(d)