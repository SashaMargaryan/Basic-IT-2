import math
n=[1,2,3,4,5,6]
s=0
for i in range(len(n)):
    if i%2!=0:
        s+=math.fabs(n[i])
        print(n[i])
print(s)
