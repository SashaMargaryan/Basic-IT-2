import math
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

f=n[-1]
for i in n:
    if i<f:
        f=i
print(f)
s=(x+f)/2

for i in n:
    if math.fabs(i)<s:
        y.append(i)
print(y)