import math

def func(x):
    k=1
    while k<10:
        if 2<x<6:
            print(k,math.log(x,4)+math.log(k))
        else:
            print(k,4*(math.pow(x,8)+math.pow(k,8)))
        k+=1

func(2)

