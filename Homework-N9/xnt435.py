a = [[1, 5.2, 3, 4],
     [1, 10.1, 7, 8],
     [5.1, 1, 3, 4],
     [6, 5.3, 5, 8]]
n = len(a)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print()

f = 0
h=1
b=5
n=len(a)
for i in range(0,n+1):
    for j in range(0,n-i):

        if int(a[i][j])%5==0:
            f = f + 1
        print(a[i][j], end=' ')

    print()
print(f)