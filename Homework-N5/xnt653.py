a = "acheallabhc"

x=[]
for i in a:

    if i=='a':
        x.append(i+"c")

f = str(''.join(map(str, x)))
print(f)

print(x)

