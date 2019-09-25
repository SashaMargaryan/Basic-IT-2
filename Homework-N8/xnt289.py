import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)

c=-9
d=9

for i in n:
    if c<(i**2)<d:
        y.append(i)
print(y)