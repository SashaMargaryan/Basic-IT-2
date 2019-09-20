a=[1,2,3,4,5,6,7,8]

k=2
f=0
s=len(a)
for i in a:
    if (i+a[-1])%k==0:

        f=f+i
        print(i)
print(f)

