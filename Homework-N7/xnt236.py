n=[1,2,3,4,5,6]

s=0
c=1

for i in n:
    if i%2!=0:
        s=s+1
        c=c*i
print(s)
print(c)