import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,40))
print(n)
m=3
for i in n:

    if i%m==0:
        y.append(i)
print(y)