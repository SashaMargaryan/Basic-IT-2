a = [1, 2, 3, 4, 5, 6, 8]
s=0
b = 0
for i in a:
    if i % 2 != 0:
        b = b + 1
        s = s + i


print(b)
print(b*s)
