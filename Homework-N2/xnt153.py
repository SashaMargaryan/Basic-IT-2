a=[1,4,5,6,9,12,3,45,20,80]

b=0

for i in a:
    if i%6==2:
        b+=i
        print(i)

print(b)