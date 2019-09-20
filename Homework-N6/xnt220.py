a=[1,2,3,4,6,-2,-8,4]
b=0
s=0
for i in a:
    if i>0:
        b=b+1

for f in a:
    if f<0:
        s=s+1
print(b,s)
