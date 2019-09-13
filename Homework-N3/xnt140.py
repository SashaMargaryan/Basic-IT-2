import math

def func(x):

    k=2

    while k<10:
        if 3<x<5:
            print(k,math.pow(x,k+6))
        elif x<=3:
            print(k,x+math.pow(k,4))
        else:
            print(k,math.pow(5,6))
        k+=1
func(3)

