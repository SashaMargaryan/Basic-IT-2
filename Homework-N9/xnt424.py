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

f = 0
d = 0
n=len(a2)
for i in range(0,n):
    for j in range( 0,i+1):

        if a2[i][j]%2 != 0:
            f = f + 1
            d = d + a2[i][j]

        print(a2[i][j], end=' ')

    print()

print(d,f)
print((d/f)**2)
