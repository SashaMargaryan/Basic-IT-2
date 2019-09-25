import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)

x = n[-1]
for i in n:
    if i > x:
        x = i
print (x)

for i in n:
    if i%2==0:
        y.append(i+x)
print(y)