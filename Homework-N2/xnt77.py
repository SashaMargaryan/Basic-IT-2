import math

x=-8

while x<8:
    if x>3:
        print(x,math.pow(x,2)+4*math.pow(x,6))
    else:
        print(x,0)
    x+=3