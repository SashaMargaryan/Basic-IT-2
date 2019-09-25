n=[1,2,3,'k','d','j']
c=[]

d=0

for i in range(len(n)):
    if n[i]=='k':
        d=i
        print(i,n[i])

for i in range(len(n)):
    if i>d:
        c.append(n[i])
print(c)
