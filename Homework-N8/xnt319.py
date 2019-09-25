import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)

for i in range(0,len(n),3):#Amn erordin veragrum enq 0
     n[i]=0

print(n)

d=n[-1]
for i in n:
    if i>d:
        x=i
print(d)

for i in n:
    if i!=0:

        y.append(i+d)
print(y)