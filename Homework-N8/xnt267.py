import random
n=int(input('n:'))
a=[]
b=[]
for i in range(n):
    a.append(random.randint(1,24))
for i in range(n):
    b.append(random.randint(1,24))

s=0
f=0
for i in a:
    if i%7==0:
        s=s+i
        print(i)
for x in b:
    if x%7==0:
        f=f+x
        print(x)

print(a)
print(b)
print(f+s)