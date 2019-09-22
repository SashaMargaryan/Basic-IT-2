import math
n=[1,2,3,4,5,6,7,8]

t=5
s=1
for i in n:
    if math.fabs(i)<t:
        s=s*i
        print(i)
print(s)
