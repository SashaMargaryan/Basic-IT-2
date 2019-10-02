def tiv_1(n):
    if n%2>0 and n!=1:
        print("parz")
    else:
        print("parz che")

def tiv_2(a):
    b=1
    while a!=0:
        x=a%10
        a=int(a/10)
        b=b*x
    print(b)


tiv_1(3)
tiv_2(222)