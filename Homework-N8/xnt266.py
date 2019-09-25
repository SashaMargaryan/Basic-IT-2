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
for i in a:
    if i%2==0:
        s=s+i
for x in b:
    if x%2!=0:
        f=f+x


print(a,b)
print(s/f)