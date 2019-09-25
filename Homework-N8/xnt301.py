import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,40))
print(n)
k=3
for i in n:
    if i>=10:
        if i%k==0:
            y.append(i)
print(y)