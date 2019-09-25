a=[1,2,3,'s','s','s','a']
s=0
c=0
for i in range(len(a)):
    if a[i]=='s':
        s=s+i
        print(i)

print(s)