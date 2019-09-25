import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)

for i in n:
    y.append(i)
print(y)

a=-5
b=6
y = [x for x in y if a<x<b]

print(y)