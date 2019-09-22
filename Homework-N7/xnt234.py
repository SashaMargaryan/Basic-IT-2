n=[1,2,3,4,5,6]

s=0
f=0
for i in n:
    if i%2!=0:
        s=s+1
        f=f+i

print(f/s)
print(s)