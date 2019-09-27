a = [[1, 2, 3, 4],
     [1, 6, 7, 8],
     [5, 1, 3, 4],
     [6, 5, 5, 8]]
n = len(a)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print()

s = 0
d = 0
for i in range(n+1):
    for j in range( i+1,n):

        if a[i][j] % 2 == 0:
            s = s + 1
            d = d + a[i][j]

        print(a[i][j], end=' ')

    print()

print(d,s)
print((d/s)**2)
