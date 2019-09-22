import random

def func(n,a=1,b=5):
    a1=[]
    for i in range(n):
        a1.append(random.randint(a,b))
    return a1
a2=[]
s=3
for i in range(s):
    a2.append(func(s))
for i in a2:
    print(i)

for i in range(len(a2)):
    su=0
    for x in range(len(a2)):
        su=su+a2[i][x]
    print(su)












