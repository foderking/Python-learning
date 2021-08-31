def straighter(li):
    print('Your answers are: ',end='')
    for he in li[:-1]:
        print(str(he) + ', ',end='')
    print('and '+ str(li[-1]))

i = 0
you = []
for yo in range(86):
    while True:
        try:
            if i == 0:
                you.append(int(input('type in your '+ str(yo + 1) +'st value : ')))
            elif i == 1:
                you.append(int(input('type in your '+ str(yo + 1) +'nd value : ')))            
            elif i == 2:
                you.append(int(input('type in your '+ str(yo + 1) +'rd value : ')))    
            else:
                you.append(int(input('type in your '+ str(yo + 1) +'th value : ')))
        except ValueError:
            print('Error: type in a valid NUMBER !!.')
            continue
        i += 1
        break
straighter(you)
