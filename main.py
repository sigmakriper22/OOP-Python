dig=[]
while True:
    a=int(input('add(1)|remove(2)|history(3) = '))
    if a==1:
        a=input('что хотите добавить?')
        dig.append(a)
        print('added')
    elif a==2:
        a=input('что хотите убрать?')
        if a in dig:
            dig.remove(a)
            print('сделано!')
        else:
            print('нету в списке')
    elif a==3:
        print(dig)
    else:
        print('не')