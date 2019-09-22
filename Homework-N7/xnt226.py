import math
n=[1,2,3,4,5,6,7]
k=5
s=0
for i in n:
    if math.fabs(i)<5:
        s=s+1
        print(i)
print(s)