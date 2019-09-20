import math
a=[1,2,3,4,5,6,7]

k=2
b=0

for i in a:
    if math.fabs(i%a[-1])>k:
        b=b+1
        print(i)

print(b)






