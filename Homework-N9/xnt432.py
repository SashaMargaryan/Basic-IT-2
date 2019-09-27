import math
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

d=0
n=len(a)
for i in range(0,n+1):
    for j in range(0,n-i):

        if (i+j)%2!= 0:
            d=d+(a[i][j]**2)


        print(a[i][j], end=' ')

    print()

print(d)
print(math.sqrt(d))
