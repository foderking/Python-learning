# The sexy all in one calculator
import sys





#repeats until a number is given & handled for value error#
def FirstSecond():
    global first
    global sec

    while True:
        print('Enter the first number'.ljust(30),end='')
        try:
            first = float(input())
        except ValueError:
            print('ERROR: You need to type in a number!!!.')
            continue
        break
    while True:
        print('Enter the second number'.ljust(30),end='')
        try:
            sec = float(input())
        except ValueError:
            print('ERROR: You need to type in a number!!!.')
            continue
        break   

def operator(var):
    global ans
    global first
    global sec
    var = var.lower()
    if var == 'd':
        ans = first / sec
        database['Division'].append(ans)
    if var == 'm':
        ans = first * sec
        database['Multiplication'].append(ans)
    if var == 'a':
        ans = first + sec
        database['Addition'].append(ans)
    if var == 's':
        ans = first - sec
        database['Subtraction'].append(ans)

def end_print():
    for ke, va in database.items():
        i = 1
        for da in va:
            print( ''.join([str(ke), ' ',str(i)]).ljust( (val_nu - 2 - len(str(da))) ,'.')  + str(da) )
            i += 1

def iterator(var):
    print(''.center(val_nu,'='))
    FirstSecond()
    operator(var)
    print('ANSWER'.ljust((val_nu - 1 - len(str(ans))),'.')+' ' + str(ans))
    print(''.center(val_nu,'_'))


val_nu = 40
val_na = 2 * val_nu
database = {'Division':[], 'Multiplication':[], 'Addition':[], 'Subtraction':[]}
while True:
    print()
    print('What operation do you want to perform? (Press enter to exit and "v" to view results)'.upper())
    print('Type "D" for Division, "M" for Multiplication, "A" for Addition, "S" for Subtraction: ', end='')
 #   print(''.center(val_nu,'_'))
    val = input()
    print()

    if val == '':
        print('Have a nice day!.')
        break
    #Division
    elif val == 'd':   
        print(''.center(val_nu,'='))
        print('Division'.center(val_nu))
        iterator(val)
    #Mulplication
    elif val == 'm':
        print(''.center(val_nu,'='))
        print('Multiplication'.center(val_nu))
        iterator(val)

    #Addition
    elif val == 'a':
        print(''.center(val_nu,'='))
        print('Addition'.center(val_nu))
        iterator(val)

    #Subtraction
    elif val == 's':
        print(''.center(val_nu,'='))
        print('Subtraction'.center(val_nu))
        iterator(val)
    #READ
    elif val == 'v':
        end_print()

    else:
        print('ERROR: Type a valid argument!!.'.center(val_nu,'.'))

