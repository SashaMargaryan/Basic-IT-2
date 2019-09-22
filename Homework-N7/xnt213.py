n=[1,2,-3,-4,-2,]
c=0
s=0
for i in n:
    if i<0:
        s+=i
        c=c+1
        print(i)
print((s/c)**2)
print(c)