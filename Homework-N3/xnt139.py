import math

def func(x):

    k=1

    while k<8:
        if 2<x<5:
            print(k,7*math.pow(math.e,k+3))
        elif 0<x<=5:
            print(k,8*x*math.pow(k,5))
        else:
            print(k,7)
        k+=1
func(9)

