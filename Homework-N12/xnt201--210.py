def xnt_201(a):

    d=0
    while a!=0:
        x=a%10
        a=int(a/10)
        d=d+1

    return d

def xnt_202(a):
    d=0
    while a!=0:
        x=a%10
        a=int(a/10)
        d=d+x
    return d

def xnt_203(a):
    b=1
    while a!=0:
        x=a%10
        a=int(a/10)
        b=b*x
    return b

def xnt_204(a):

    while a!=0:

        x=(a%10)
        a = a // 10
        print(x,end='')

def xnt_205(a):
    f=a
    x=0
    d=0
    while a!=0:

        x = (a % 10)
        d=d*10
        d=d+x
        a = a // 10

    return d

def xnt_206(a):

    x=0
    while a!=0:
        x=(x*10)+(a%10)
        a=a//10

    return x

def xnt_207(a):

    while a!=0:
        x=a%10
        if x==2:
            return True
        a=a//10
    return False


def xnt_208(a):
    s=a
    b=0
    x=0
    while a!=0:
        x=(x*10)+(a%10)
        a=a//10

    if x==s:
        return True
    else:
        return False

def xnt_209(a):
    while a!=0:
        x=a%10
        if x%2!=0:
            return True
        a=a//10
    return False

def xnt_210(a):
    s=0
    d=0
    while a!=0:
        x=a%10
        if x%2!=0:
            s=s+x
        if x%2==0:
            d=d+x
        if d==s:
            return True
        a=a//10
    return False


print(xnt_201(222))
print(xnt_202(2222))
print(xnt_203(22))
print(xnt_204(123))
print(xnt_205(1234))
print(xnt_206(1234))
print(xnt_207(112))
print(xnt_208(1221))
print(xnt_209(221))
print(xnt_210(122111))

