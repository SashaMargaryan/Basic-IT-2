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

y = [x for x in y if x%2== 0]

print(y)