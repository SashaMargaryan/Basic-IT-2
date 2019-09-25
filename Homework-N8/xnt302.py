import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,40))
print(n)

for i in n:
    if i>=10:
        if i%5==2:
            y.append(i)
print(y)