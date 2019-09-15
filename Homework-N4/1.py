balans=1000
while True:
    try:
        i=int(input("o-exit:1-stugel:2-hanel:"))
    except ValueError:
        print("nermuchel tiv:")
        continue

    if i==0:
        break
    elif i==1:
        print(balans)
    elif i==2:
        try:
            cesh=int(input("kanxik:"))
        except ValueError:
            print('nermuchel tiv:')
            continue
        if cesh>balans:
            print('gmar cka:')
        else:
            print("kanxikachm@ hajoxvele:")
            balans=balans-cesh
print("hajoxutyun")