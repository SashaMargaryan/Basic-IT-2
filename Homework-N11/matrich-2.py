a=[[1,2,3,4],
   [5,6,7,8],
   [9,8,7,6],
   [4,3,2,1]]
s=len(a)

k=9
d=0

a[1][1]=a[1][2]=a[2][1]=a[2][2]=k
k=k^d
d=d^k
k=k^d


for i in range(s):
    for j in range(s):
        print(a[i][j],end=' ')
    print()

