import random

x=int(input("x:"))
n=[]

y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)


for i in n:
    if i%6==1:
        y.append(i)
print(y)