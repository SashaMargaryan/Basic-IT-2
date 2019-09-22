x=[1,2,-3,-4,5,6,-8]
y=[1,2,3,4,-5,-6]
s=0
c=0

for i in x:
    if i<0:
        s=s+1
print(s)

for x in y:
    if x<0:
        c=c+1

print(c)

