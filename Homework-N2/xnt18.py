import math

x=float(input("nermchel:x"))
z=float(input('nermuchel:z'))

if 1<=x<=7:
    print(math.fabs(x)+2*math.fabs(z)**4+math.pow(math.e,x+1))
else:
    print(1-math.cos(2)*math.pow(x,7)+math.pow(z,7)/ 1+math.cos(2)*math.pow(x,7)+math.pow(z,7))