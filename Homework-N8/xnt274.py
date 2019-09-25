
a=[1,2,3,'h','f','j']

s=0
d=0
f=0

for i in range(len(a)):
    if a[i]=="h":  #gtel em h-i indeqs@
        d=i
        print(d,a[i])


for i in range(len(a)):
    if i>d:   # gtel em h-ic barchr indeqsner@
        s=s+i
        f=f+1
        print(i,a[i])

print(s/3)

