a = [[1, 0, 3, 4],
     [1, 6, 7, 8],
     [5, 1, 3, 4],
     [6, 6, 5, 8]]
n = len(a)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print()
f = 0

n=len(a)
for i in range(n):
    for j in range(n-i-1,n):

        if (i+j)%2!= 0:
            f = f + 1

        print(a[i][j], end=' ')

    print()

print(f)
