n=[1,2,3,4,5,9,9]
s=0
c=0
k=3
for i in range(len(n)):
    if n[i]%k==0:
        s=s+1
        c=c+n[i]
        print(n[i])

print(s)
print(c/s)