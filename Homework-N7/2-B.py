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

for x in range(len(a2)):
    sum=0
    for i in range(len(a2)):
        sum=sum+a2[i][x]
    print(sum)