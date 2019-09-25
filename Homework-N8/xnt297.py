import random
import math
x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)

for i in n:
    y.append(i)
print(y)

k=5
y = [x for x in y if math.fabs(x) > k]

print(y)