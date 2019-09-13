a=2
b=6
c=9

if a>b and a>c and b>c:
    print(a,b,c)
elif a<b and b>c and a>c:
    print(b,a,c)
elif a<c and b<c and a<b:
    print(c,b,a)