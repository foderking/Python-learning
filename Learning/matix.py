matr = []
for name in range(1,8) :
    if name ==1:
       name = input('Enter the ' + str(name)+'st' + ' number:')
    elif name == 2:
        name = input('Enter the ' + str(name)+'nd' + ' number:')
    elif name ==3:
       name = input('Enter the ' + str(name)+'rd' + ' number:')
    else:
       name = input('Enter the ' + str(name)+'th' + ' number:')
    matr = matr + [int(name)]

#print(matr)
print('Your numbers are: ', end='')
for ex in matr:
    print(ex,end=' | ')
