def func(mard):
    while True:
        try:
            i=int(input(mard))
            return i
        except ValueError:
            print(('nermchel tiv:'))
            continue
hert=0
while True:
    i=func('exit-0:amragrel hert-1:hertm mardkanch qanak-2:cexarkel hert@-3')
    if i==0:
        break
    elif i==1:
        gal=func("avelanum en:")
        if hert==gal:
            print('hert cka:')
        elif hert>=gal or hert<=gal:
            print("hert@ avelanume:",gal,'ov')
            hert=hert+gal
    elif i==2:
        print(hert)
    elif i==3:
        gnal=func("hert@ nvazume:")
        if hert>=gnal or hert<=gnal:
            print('nvazume:',gnal,'ov')
            hert=hert-gnal
        elif hert<0:
            print('mard cka:')
            break
print('hajoxtyun')

