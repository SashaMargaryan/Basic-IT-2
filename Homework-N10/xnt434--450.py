import math
def func_m(func_nam,arg,ret):
    if ret==func_nam(arg): #dekorator
        return True
    return False

def xnt_434(a):
    n=len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j],end='')
        print()
    print()

    s=0
    for i in range(1,n):
        for j in range(n-i,n):
            if 5.4<a[i][j] and a[i][j]<14.5:
                s=s+a[i][j]
            print(a[i][j],end='')
        print()
    return s

def xnt_435(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end='')
        print()
    print()

    f=0
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if int(a[i][j])%5==0:
                f=f+1
            print(a[i][j],end='')
        print()
    return f

def xnt_436(a):

    n = len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end='')
        print()
    print()

    c=4
    b=10
    cm=0
    bm=0
    for i in range(1,n):
        for j in range(0,i):
            if c<a[i][j] and b>a[i][j]:
                cm=cm+1
                bm=bm+a[i][j]
            print(a[i][j],end='')
        print()
    return bm/cm

def xnt_437(a):
    n=len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j],end='')
        print()
    print()

    f1=0
    for i in range(0,n):
        for j in range(0,i+1):
            if a[i][j]==int(a[i][j]):

                f1=f1+ math.pow(a[i][j],2)
            print(a[i][j],end='')
        print()
    return int(math.sqrt(f1))

def xnt_438(a2):
    n=len(a2)
    for i in range(n):
        for j in range(n):
            print(a2[i][j],end='')
        print()
    print()

    f2=0
    for i in range(1,n):
        for j in range(0,i):
            if a2[i][j]>0 and i%2==0 :
                f2=f2+1
            print(a2[i][j],end='')
        print()
    return f2

def xnt_439(a2):
    n=len(a2)
    for i in range(n):
        for j in range(n):
            print(a2[i][j],end='')
        print()
    print()

    f3=1
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (i+j)%2!=0:
                f3=f3*a2[i][j]
            print(a2[i][j],end='')
        print()
    return f3
def xnt_440(a2):
    n=len(a2)
    for i in range(n):
        for j in range(n):
            print(a2[i][j],end='')
        print()
    print()

    f4=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (i+j)%2==0:
                f4=f4+a2[i][j]
            print(a2[i][j],end='')
        print()
    return f4

def xnt_441(a2):
    n=len(a2)
    for i in range(n):
        for j in range(n):
            print(a2[i][j],end='')
        print()
    print()

    f5=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a2[i][j]>0:
                f5=f5+math.pow(a2[i][j],2)
            print(a2[i][j],end='')
        print()
    return int(math.sqrt(f5))

def xnt_442(a2):
    n=len(a2)
    for i in range(n):
        for j in range(n):
            print(a2[i][j],end='')
        print()
    print()

    f6=0
    mi=0
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if a2[i][j]<0:
                mi=mi+1
                f6=f6+a2[i][j]
            print(a2[i][j],end='')
        print()
    return int(f6/mi)

def xnt_443(a3):
    n=len(a3)

    for i in range(n):
        for j in range(n):
            print(a3[i][j],end='')
        print()
    print()

    f7=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a3[i][j]==0:
                f7=f7+1
            print(a3[i][j],end='')
        print()
    return f7

def xnt_444(a4):
    n=len(a4)
    for i in range(n):
        for j in range(n):
            print(a4[i][j],end='')
        print()
    print()

    f8=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a4[i][j]<0 and i%2!=0:
                f8=f8+1
            print(a4[i][j],end='')
        print()
    return f8

def xnt_445(a4):
    n=len(a4)
    for i in range(n):
        for j in range(n):
            print(a4[i][j],end='')
        print()
    print()
    f9=0
    k=4
    for i in range(1,n):
        for j in range(0,i):
            if math.fabs(a4[i][j])>k:
                f9=f9+1
            print(a4[i][j],end='')
        print()
    return f9

def xnt_446(a5):
    n=len(a5)
    for i in range(n):
        for j in range(n):
            print(a5[i][j],end='')
        print()
    print()

    ai=0
    bi=7
    f10=0
    for i in range(0,n):
        for j in range(i,n):
            if ai < a5[i][j] and  a5[i][j] < bi:
                f10=f10+a5[i][j]
            print(a5[i][j],end='')
        print()

    return f10

def xnt_447(a5):
    n=len(a5)
    for i in range(n):
        for j in range(n):
            print(a5[i][j],end='')
        print()
    print()

    ab=5
    h=1
    for i in range(0,n):
        for j in range(n-i-1,n):
            if a5[i][j]<ab:
                h=h*a5[i][j]
            print(a5[i][j],end='')
        print()
    return h

def xnt_448(a5):
    n=len(a5)
    for i in range(n):
        for j in range(n):
            print(a5[i][j],end='')
        print()
    print()

    y=0
    u=0

    for i in range(0,n):
        for j in range(i,n):
            if (i+j)%2==0:
                y=y+1
                u=u+a5[i][j]
            print(a5[i][j],end='')
        print()
    return u/y

def xnt_449(a5):
    n=len(a5)
    for i in range(n):
        for j in range(n):
            print(a5[i][j],end='')
        print()
    print()

    p=0
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if int(a5[i][j])%4==0:
                p=p+a5[i][j]
            print(a5[i][j],end='')
        print()
    return p


def xnt_450(a6):
    n=len(a6)
    for i in range(n):
        for j in range(n):
            print(a6[i][j],end='')
        print()
    print()

    t=0
    for i in range(1,n):
        for j in range(n-i,n):
            if a6[i][j]==float(a6[i][j]):

                t=t+(a6[i][j])

            print(a6[i][j],end='')
        print()
    return (t%2)-1

a6=[[1,2.2,3,4],
    [4,5,6,7],
    [8,9,7,4.2],
    [1,2,3.2,4.5]]

a5=[[1,2.2,3,4],
    [4,5,6,7],
    [8,9,7,4],
    [1,2,3,4]]

a4=[[1,2,-3,-4],
    [4,5,-6,-7],
    [7,8,9,-4],
    [7,8,3,6]]

a3=[[1,2,3,0],
    [4,5,6,0],
    [7,8,9,5],
    [3,2,1,0]]

a2=[[-1,2,3,-3],
    [5,6,7,8],
    [-9,8,7,4],
    [1,-2,3,4]]

a=[[1,2,3,4],
   [4,5,6,7],
   [10,14,15,6],
   [15.2,10,8,7]]

print(func_m(xnt_434,a,38))
print(func_m(xnt_435,a,2))
print(func_m(xnt_436,a,8.0))
print(func_m(xnt_437,a,27))
print(func_m(xnt_438,a2,1))
print(func_m(xnt_439,a2,-168))
print(func_m(xnt_440,a2,11))
print(func_m(xnt_441,a2,11))
print(func_m(xnt_442,a2,-5))
print(func_m(xnt_443,a3,2))
print(func_m(xnt_444,a4,2))
print(func_m(xnt_445,a4,4))
print(func_m(xnt_446,a5,29.2))
print(func_m(xnt_447,a5,384))
print(func_m(xnt_448,a5,4.5))
print(func_m(xnt_449,a5,12))
print(func_m(xnt_450,a6,0.8999999999999986))
print(xnt_450(a6))
