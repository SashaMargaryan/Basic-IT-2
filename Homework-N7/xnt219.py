n=[1,2,3,4,5,6,9]
k=3
s=0
for i in range(len(n)):
    if n[i]%k==0:
        s=s+1
        print(n[i])
print(s)