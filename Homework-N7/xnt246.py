n=[1,2,3,4,5,6,7,8]
s=2
c=0
a=0
for i in range(len(n)):
    f=n[i]
    if f%4==s:
        c=c+1
        a=a+i
        print(i)

print(a/c)