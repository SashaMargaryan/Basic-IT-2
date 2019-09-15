def func(mes):
    while True:
        try:
            i=int(input(mes))
            return i
        except ValueError:
            print('nemuchel tiv')
            continue
balans=1000
while True:
    i=func('0-exit:1-balans:2-verchnel:3-avelachel')
    if i==0:
        break
    elif i==1:
        print(balans)
    elif i==2:
        cesh=func('verchnel:')
        while True:
            if cesh==0:
                print('chexarkel')
                break
            elif cesh<0:
                cesh=func('nermuchel drakan tiv:')
                if cesh>balans:
                    print("gumar chka:")
                else:
                    print('kanxikachum@ stacvel e:')
                    balans=balans-cesh
    elif i==3:
        try:
            avel=int(input("avelachnel gumar:"))
        except ValueError:
            print('nermuchel tiv:')
            continue
        print('poxanchum@ hajoxvel e:')
        balans=balans+avel
print('hajox')


