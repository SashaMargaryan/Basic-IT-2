import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)

for i in range(len(n)):
    if n[i]!=i:
        y.append(n[i])
print(y)