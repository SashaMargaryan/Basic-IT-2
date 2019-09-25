import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)

p=3
for i in n:
    if i%p==0:
        y.append(i)
print(y)
