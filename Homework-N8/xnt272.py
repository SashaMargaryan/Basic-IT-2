a=[1,2,3,'b','b','b',]
s=0
c=0

for i in a:
    s = s + 1
    if i=="b":
        c=c+1


if s/2==c:
    print(True)

elif s/2!=c:

    print(False)


