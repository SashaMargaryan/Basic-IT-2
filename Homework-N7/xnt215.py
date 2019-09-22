n=[1,2,3,4,5,6,7,8,9,10,1,1,1]
s=0
for i in range(len(n)):
    if i%2==0:
        s+=n[i]
        print(n[i])
print(s)