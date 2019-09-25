import random

x=int(input("x:"))
n=[]
y=[]

for i in range(x):
    n.append(random.randint(-10,10))
print(n)




for i in range(len(n)):
    if n[i]%2==0:
        y.append(n[i])

        del [i]
print(y)

