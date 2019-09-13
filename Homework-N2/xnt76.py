import math

x=-5

while x<5:
    if x>0:
        print(x,math.pow(x,2)+4*math.pow(x,6))

    else:
        print(x,0)

    x+=2
