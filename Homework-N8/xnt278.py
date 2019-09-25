n=[1,2,3,'d','d','j']
c=[]

for i in range(len(n)):
    if i%2!=0:
        c.append(n[i])

        print(n[i],i)

print(c)