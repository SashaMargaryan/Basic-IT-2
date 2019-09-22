n=[2,3,4,5,6,7,8,1,1,1]

s=1
for i in range(len(n)):
    if i%2!=0:
        s*=(n[i]**2)
        print(n[i])
print(s)
