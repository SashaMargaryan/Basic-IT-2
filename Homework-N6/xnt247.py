a=[1,2,3,90,5,6,7,90,9,10,11,20,30]
f=0
b=0

for i in a:
    if i>a[-1]:
        b=b+1
        f=f+i
        print(i)
print(b)
print(f/b)



