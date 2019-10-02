def rec_1(n):
    if n==1:
        return 1
    return n + rec_1(n-1)

def tox_2(a):
    if len(a)==0:
        return
    print(a[0])
    tox_2(a[1:])


def file_3():  #1 file
    s=open('1','r')
    f = s.readline().split(',')
    print(f)
    x = f[-1]

    for i in f:
        if i > x:
            x = i

    f = s.readline().split(',')
    print(f)
    j = f[-1]

    for m in f:
        if m < j:
            j = m
        return int(x) * int(j)
    s.close()

def file_4():   # 2 file
    s1=open('2','r')
    f1=s1.readline().split(',')
    print(f1)

    c=0
    for i in range(len(f1)):
        if f1[i]=='a':
            c=c+1
    print(c)
    f1 = s1.readline().split(',')
    print(f1)
    f=0
    for j in range(len(f1)):
        if f1[j]=="z":
            f=f+1
    print(f)
    f1 = s1.readline().split(',')
    print(f1)
    y=0
    for z in f1:
        y=y+1
    print(y)

    s1.close()

def file_5(z): #3 file
    s2=open('3','a')
    k=0
    for i in z:
        k=k+1

    s2.write(str(k))

    s2.close()

def file_6():  #4 file
    s3=open('4','r')
    f3=s3.readline()
    print(f3)

    g=0
    for i in range(len(f3)):

        if i>10:

            g=g+1
    print(g)

    s3.close()

def file_7(): #5 file
    s4=open("5",'r')
    f4=s4.readline().split(',')
    print(f4)

    x=0
    z=0
    for i in range(len(f4)):
        if i%2!=0:
            x=x+1
            z=z+int(i)
    print(z/x)

    s4.close()


print(rec_1(5))

tox_2('abcdfg')

print(file_3())

file_4()

z=[1,2,3,4,5,6,7,8,9]
file_5(z)

file_6()

file_7()