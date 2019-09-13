import math
a=float(input('nermuchel:a'))
b=float(input('nermuchel:b'))
x=float(input('nermuchel:x'))

if math.pow(a,2)+math.pow(b,2)>5:
    print(3*(math.pow(math.e,a)-math.pow(math.e,x))+math.log(math.pow(a,2)+math.pow(b,2)+5,3))

elif math.pow(a,2)+math.pow(b,2)<1:
    print(math.cos(4)*(a+b)-4*math.cos(2)*(a+b)+3/math.cos(4)*(a+b)+4*math.cos(2)*(a+b)+3)

else:
    print(-3)