import random
n=int(input('n:'))
a=[]
b=[]
for i in range(n):
    a.append(random.randint(1,10))
for i in range(n):
    b.append(random.randint(1, 10))
k=2
s=0
f=0
for i in a:
    if i%k==0:
        s=s+i
        print(i)
for x in b:
    if x%k==0:
        f=f+x
        print(x)


print(a,b)
print(s+f)