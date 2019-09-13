import math

a=float(input('nermuchel:a'))
b=float(input('nermuchel:b'))
x=float(input('nermuchel:x'))

if a+math.fabs(b)<-5:
    print(math.pow(math.e,math.sqrt(a+x))*math.cos(2)*(a+b+x)/2)

elif a+math.sqrt(b)>2:
    print(math.atan(a)+math.atan(x)**3)

else:
    print(a+math.sqrt(b))