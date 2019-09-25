import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-1000,9000))
print(n)

for i in n:
    if i>999:
        if i%5==0 and i%3==0:
            y.append(i)
print(y)