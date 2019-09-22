n=[1,2,3,-4,-5,-6,-5]

s=0
c=0
for i in n:
    if i>0:
        s=s+1
for i in n:
    if i<0:
        c=c+1

print(s,c)
