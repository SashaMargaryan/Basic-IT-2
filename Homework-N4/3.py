hert=0
while True:
    try:
        i=int(input("exit-0:amragrel hert-1:hertm mardkanch qanak-2:cexarkel hert@-3:"))
    except ValueError:
        print("nermuchel tiv:")
        continue
    if i==0:
        break
    elif i==1:
        try:
            gal=int(input("hert pahel:"))
        except ValueError:
            print("nermuchel tiv:")
            continue
        if hert==gal:
            print("hert cka:")
        elif hert<=gal or hert>=gal:
            print("hert@ avelachele:",gal,'-ov')
            hert=hert+gal
    elif i==2:
        print(hert)
    elif i==3:
        try:
            gnal=int(input('hert@ pakasel:'))
        except ValueError:
            print("nermuchel tiv:")
            continue
        if hert>=gnal or hert<=gnal:
            print('nvazume:',gnal,'-ov')
            hert=hert-gnal
        elif hert<0:
            print("mard cka")
            break

print("ctesutyun:")


