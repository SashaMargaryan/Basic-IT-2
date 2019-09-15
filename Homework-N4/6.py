def func(pox):
    while True:
        try:
            i=int(input(pox))
            return  i
        except ValueError:
            print("nemuchel tiv:")
            continue
dram=0
dolar=0
rubli=0
while True:
    i=func("0-durs:1-hasiv:2-avelacnel:3-hanel:")
    if i==0:
        break
    elif i==1:
        print(dram,'-dram',dolar,'-dolar',rubli,'-rubli')
    elif i==2:
        avel=func("0-dram:1-dolar:2-rubli")

        while True:

            if avel==0:
                gum1=func("gumar:")
                print('avelachel:',gum1)
                dram=dram+gum1
                break
            elif avel==1:
                gum2=func("gumar:")
                print("avelanum:",gum2)
                dolar=dolar+gum2
                break
            elif avel==2:
                gum3=func("gumar:")
                print("avelachel",gum3)
                rubli=rubli+gum3
                break
            elif  avel>=0<=2:
                break


    elif i==3:
        pakas=func("0-dram:1-dolar:2-rubli")
        while True:

            if pakas==0:
                gum1=func('gumar:')
                print("pakasel:",gum1)
                dram=dram-gum1
                break
            elif pakas==1:
                gum2=func('gmar:')
                print("pakasel:",gum2)
                dolar=dolar-gum2
                break
            elif pakas==2:
                gum3=func("gumar:")
                print('pakasel:',gum3)
                rubli=rubli-gum3
                break
            elif pakas>=0<=2:
                break
print("hajoxutyun")

