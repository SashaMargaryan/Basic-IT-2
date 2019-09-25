import random
n=int(input('n:'))
a=[]
b=[]
for i in range(n):
    a.append(random.randint(1,10))
for i in range(n):
    b.append(random.randint(1, 10))

s=0
f=0
for i in range(len(a)):
    if a[i]%2==0:
        s=s+a[i]
for x in range(len(b)):
    if b[x]%2!=0:
        f=f+b[i]


print(a,b)
print(s+f)