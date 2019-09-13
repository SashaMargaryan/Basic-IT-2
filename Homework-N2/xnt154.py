a=[1,4,5,6,9,12,3,45,20,80,120,145]

b=0

for i in a:
    if i%6==3:
        b+=i
        print(i)

print(b)