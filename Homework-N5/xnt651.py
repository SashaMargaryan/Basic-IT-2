a = "hellbhh"

x=[]
for i in a:
    s=a.count(i)#hasvume te vor tarich qani hat ka
    if s==1:
            x.append(i)

f= str(''.join(map(str,x)))#darchnume mi bar
print(f)

print(x,len(x))













