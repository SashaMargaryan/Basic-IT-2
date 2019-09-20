import math
a=[1,2,3,4,6,-2,4,9]
b=0
s=0
for i in range(len(a)):
    if i%2!=0:


        b=b+math.fabs(i)
print(b)