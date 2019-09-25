import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)

a=-5
b=5
for i in n:
    if a<i<b:
        y.append(i)
print(y)
