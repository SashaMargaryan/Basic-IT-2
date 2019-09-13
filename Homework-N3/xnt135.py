import math

def func(k,x):
    if x>1:
        print(math.pow(x,k-1))
    elif x<3:
        print(x*math.pow(k,3))
    else:
        print(math.pow(10,-6))

func(1,1)
func(2,2)
func(3,3)
func(4,1)