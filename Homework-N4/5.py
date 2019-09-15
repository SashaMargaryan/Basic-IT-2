dram=0
dolar=0
rubli=0
while True:
    try:
        i=int(input("0-durs:1-hasiv:2-avelacnel:3-hanel:"))
    except ValueError:
        print('nermuchel tiv:')
        continue
    if i==0:
        break
    elif i==1:
        print('dram:',dram,'dolar:',dolar,'rubli',rubli)
    elif i==2:
        while True:
            try:
                avel=int(input('0-dram:1-dolar:2-rubli'))
            except ValueError:
                print("nermchel tiv:")
                continue

            if avel==0:
                try:
                    gumar0=int(input('gmar:'))
                except ValueError:
                    print('nerm tiv:')
                    continue
                dram=dram+gumar0
                break
            elif avel==1:
                try:
                    gumar1=int(input('gumar:'))
                except ValueError:
                    print("nermuchel tiv:")
                    continue
                dolar=dolar+gumar1
                break
            elif avel==2:
                try:
                    gumar2=int(input('gumar:'))
                except ValueError:
                    print("nermuchel tiv:")
                    continue
                rubli=rubli+gumar2
                break

    elif i==3:
        while True:
            try:
                pak=int(input("0-pakas-D:1-pakas-$:2-pakas-R:"))
            except ValueError:
                print('nermuchel tiv:')
                continue

            if pak==0:
                try:
                    gumar3=int(input('gumar:'))
                except ValueError:
                    print('nermuchel gumar:')
                    continue
                dram=dram-gumar3
                break

            elif pak==1:
                try:
                    gumar4=int(input('gumar:'))
                except ValueError:
                    print('nermuchel tiv:')
                    continue
                dolar=dolar-gumar4
                break

            elif pak==2:
                try:
                    gumar5=int(input('gumar;'))
                except ValueError:
                    continue
                rubli=rubli-gumar5
                break

print('hajox')


