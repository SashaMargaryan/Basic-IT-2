n=[1,2,3,4,5,6]
f=0
c=0
for i in range(len(n)):
    s=i*n[i]

    if s%3==2:
        f=f+1
        c=c+(n[i]**2)

        print(n[i])

print(c/f)
print(f)