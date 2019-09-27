a = [[1, 2, 3, 4],
     [1, 6, 7, 8],
     [5, 1, 3, 4],
     [6, 6, 5, 8]]
n = len(a)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print()

s = 0
k = 2
d = 0

for i in range(1, n):
    for j in range(0, i):
        if a[i][j] % 5 == 0:
            s = s + 1
            d=d+a[i][j]

        print(a[i][j], end=' ')

    print()

print(s,d)
print(d/s)