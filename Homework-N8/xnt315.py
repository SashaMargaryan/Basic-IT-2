import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)
b=1
for i in n:
    if i>b:
        if i>0:
            print(i)
    elif i<b:
        if i<0:
            print(i)