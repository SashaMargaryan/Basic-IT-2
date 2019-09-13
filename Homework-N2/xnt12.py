import math
a=float(input('nermuchel:a'))
x=float(input('nermuchel:x'))

if -5<=x<=5:
    print(1+math.pow(a,6))


elif x>5:
    print(str(math.cos(math.log(2))*math.fabs(x)+math.pow(x,6)))
else:
    print(a)