# This program should be able to create three lists to store the scores of 5 different students, and should be able to print the values.
########################
#input name
# store name as part of list
# put in valule for subjects
# go back
# diplay available names
# display scores for selected names
########################
    # while True:
    #     if varname in Names:
    #         print()
    #         print('"'+ varname + '"s record already exists. Do you want to replace it?.')
    #         print('Press "y" to replace, and press any other key to not: ',end='')
    #         elp = input()
    #         if elp == 'y':
    #             del Inputs[int(Names.index(varname))]
    #             Names.remove(varname)
    #     Names += [varname]
    #     for su in subjects :
    #         print('Enter in your score for ' + su + ': ',end ='')
    #         subjvar += [input()]
    #     Inputs += [subjvar]
    #     break





import sys

Names = []
Inputs = []
subjects = ['Maths','Chemistry','Physics','English','Futher Maths','Computer Science', 'Anime','Feat Scaling']

def first():
    global Names
    global Inputs
    subjvar = []
    print()

    varname = input('Please input a your name (Press enter to exit): ')
    #adds the value of the name and subjects scores to the general name and subject list#
    while varname != '':
        if varname not in Names:
            Names += [varname]
            for su in subjects :
                print('Enter in your score for ' + su + ': ',end ='')
                subjvar += [input()]
            Inputs += [subjvar]
            break
    #replaces an already inputed value if the users chooses#
        else:
            print()
            print('"'+ varname + 's" record already exists. Do you want to replace it?.')
            print('Press "y" to replace, and press any other key to exit: ',end='')
            elp = input()
            if elp == 'y':
                del Inputs[int(Names.index(varname))]
                Names.remove(varname)
                continue
            else:
                break
    if varname == '':
      print('Youve exited')

def Printer():
    while True:
        print('Enter in the students name (Press enter to exit): ',end='')
        naem = input()
        if naem in Names:
            ind = int(Names.index(naem))
            print(naem + 's scores are: ')
            f = 0
            for sp in subjects :
                print(sp+ ' :' + Inputs[ind][f] )
                f+=1
        elif naem =='':
            print('Youve exited')
            break
        else:
            print(naem + ' Isnt in our records.')
    print()


while True:
    begin = input('Enter "w" for "write" mode, and "r" for "read" mode (Press enter to exit): ')
    if begin == 'w':
        first()
    elif begin == 'r':
        print()
        if Names == []:
            print('Our records are empty!!')
        else:
            print('Available records are: ',end='')
            print(Names)
            Printer()
    elif begin == '':
        break
    else:
        print('Error: Type in a valid input!.')
        continue
    print()
print()
print('Thank you for using this apllication! :)')