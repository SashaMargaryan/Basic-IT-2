x=[1,2,3,4,5]
y=[1,2,3,4,5,-2]
s=0
c=1

for i in x:
    s=s+i

for x in y:
    if x>0:
        c=c*x

print(c/s)
