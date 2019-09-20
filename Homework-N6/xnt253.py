x = [1,2,6,3,4,5,20]
c = 0
for i in x:

    if i >c:
        c= i
print(c)

x = [1,2,6,3,4,5,20]
y = 20
for i in x:

    if i < y:
        y = i
print(y)

print(c+y)