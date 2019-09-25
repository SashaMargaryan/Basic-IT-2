import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,45))
print(n)

for i in n:
    y.append(i)
print(y)

y = [x for x in y if x%7==0]

print(y)