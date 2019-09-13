import math

def func(x):

    k=2
    while k<7:
        if x<6:
            print(k,math.pow(x,k)+k)
        else:
            print(k,math.log(k,5))
        k+=1
func(2)