import math

def func(k,x):
    if x>1:
        print(math.pow(x,k-1))
    elif 0<x<5:
        print(x*math.pow(k,3))
    else:
        print(math.pow(10,-6))

func(1,2)
func(2,3)
func(8,1)
