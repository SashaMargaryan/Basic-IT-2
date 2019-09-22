n=[3,2,3,4,5,6]
s=0
d=1
for i in range(len(n)):
    f=i+n[i]
    if f%3==0:
        s=s+(n[i]**2)
        print(n[i])
print(s)