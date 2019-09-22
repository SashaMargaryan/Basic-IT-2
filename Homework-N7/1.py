import random

def func(n,a=1,b=20):
    ar=[]
    for i in range(n):
        ar.append(random.randint(a,b))
    return ar
a2=[]

s=2
for i in range(s):
    a2.append(func(s))
for i in a2:
    print(i)

su=1
for i in range(len(a2)):
    for j in range(len(a2[i])):

        su=su*a2[i][j]

print(su)


