n=[1,2,3,'d','k','j']

s=0
d=0

for i in range(len(n)):
    if n[i]=="k":
        d=i
        print(d,n[i])

for i in range(len(n)):
    if i<d:
        s=s+1
        print(i,n[i])

print(s)