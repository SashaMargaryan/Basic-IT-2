a = [[11, 12, 13],
     [21, 22, 23],
     [31, 32, 33]]
d=2
k=0
s=len(a)
a[1][1]=d
d=d^k
k=k^d
d=d^k

for i in range(s):
    for j in range(s):
        print(a[i][j],end=' ')
    print()


