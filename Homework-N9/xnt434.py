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
h=1
b=5
n=len(a)
for i in range(1,n):
    for j in range(n-i,n):


        print(a[i][j], end=' ')

    print()
print()
