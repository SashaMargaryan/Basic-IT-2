a='heloz'
b='hellozz'
x=[]
for i in a:
        s=b.count(i)
        if s==1:
                x.append(i)

f = str(''.join(map(str, x)))
print(f)

print(x)






