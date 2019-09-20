x=[1,2,3,4,5]
y=[1,2,3,4,5]
b=0
c=0
for i in range(len(x)):
    if x[i]%2==0:
        b=b+1
        c=c+i
        print(i)
print(b,c)
f=0
d=0
for i in range(len(x)):
    if x[i]%2!=0:
        f=f+1
        d=d+i
print(f,d)

print(d+c)