import sys

Database = {'Default':[21,22,23,24,25,26,27]}
subjects = ('Maths','Chemistry','Physics','English','Futher Maths','Computer Science', 'Anime')

def first():
    subjvar = []
    print()
    while True:
        varname = input('Please input a your name (Press enter to exit): ')
        if varname.isalpha():
            break
        print('Type in a valid alphabetic character!')
    #adds the value of the name and subjects scores to the general name and subject list#
    while varname != '':
        if varname not in Database:
            for su in subjects :
                while True:
                    print('Enter in your score for ' + su + ': ',end ='')
                    inputs = input()
                    if not inputs.isdecimal():
                        print('Type in a valid number')
                        continue
                    elif inputs.isspace():
                        print('Type in a number')
                        continue
                    subjvar += [inputs]
                    break
            Database[varname] = subjvar
            break
    #replaces an already inputed value if the users chooses#
        else:
            print()
            print('"'+ varname + '\'s" record already exists. Do you want to replace it?.')
            elp = input('Press "y" to replace, and press any other key to exit: ')
            if elp == 'y':
                del Database[varname]
                continue
            else:
                break
    if varname == '':
      print('You\'ve exited')

def Printer():
    while True:
        print('Enter in the students name (Press enter to exit): ',end='')
        naem = input()
        if naem in Database:
            strin = naem + '\'s scores'
            print(''.upper().center(40,'='))
            print(strin.upper().center(40))
            print(''.upper().center(40,'='))
            i = 0
            for sp in subjects :
                print(sp.ljust(30) + '||' + str(Database[naem][i]).rjust(8) )
                i+=1
        elif naem =='':
            print('You\'ve exited')
            break
        else:
            print(naem + ' Isn\'t in our records.')
    print()


while True:
    begin = input('Enter "w" for "write" mode, and "r" for "read" mode (Press enter to exit): ')
    if begin == 'w':
        first()
    elif begin == 'r':
        print()
        if Database == {}:
            print('Our records are empty!!')
        else:
            print('Available records are: ',end='')
            print(list(Database.keys()))
            Printer()
    elif begin == '':
        break
    else:
        print('Error: Type in a valid input!.')
        continue
    print()
print()
print('Thank you for using this apllication! :)')