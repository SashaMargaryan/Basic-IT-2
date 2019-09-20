import math
a=[1,2,-4,-6]
k=5
b=0
for i in a:
    if math.fabs(i)<k:
        b=b+1

print(b**3)
