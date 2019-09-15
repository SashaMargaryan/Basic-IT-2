import math

x=10
while x<20:
    if x>12:
        print(x,3*math.log(x,3)*x)
    else:
        print(x,math.pow(x,3))
    x+=2