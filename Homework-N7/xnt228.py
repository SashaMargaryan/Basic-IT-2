n=[1,2,3,4,5,6]
k=2
s=0
for i in range(len(n)):
    if n[i]%k==0:
        s=s+n[i]
        print(n[i])
print(s)