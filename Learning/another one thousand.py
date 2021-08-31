import sys

def winner():
    em = ('x','0')
    for val in em:
    #slash 1
        if da[1][1] == val and da[2][2] == val and da[3][3] == val:
            print(val + ' is the winner! ')
            sys.exit()
    #SLASH 2
        elif da[1][3] == val and da[2][2] == val and da[3][1] == val:
            print(val + ' is the winner! ')
            sys.exit()
    #horizontal
        elif da[1][1] == val and da[1][2] == val and da[1][3] == val:
            print(val + ' is the winner! ')
            sys.exit()
        elif da[2][1] == val and da[2][2] == val and da[2][3] == val:
            print(val + ' is the winner! ')
            sys.exit()
        elif da[3][1] == val and da[3][2] == val and da[3][3] == val:
            print(val + ' is the winner! ')
            sys.exit()                        
    #vertical
        elif da[1][1] == val and da[2][1] == val and da[3][1] == val:
            print(val + ' is the winner! ')
            sys.exit()
        elif da[1][2] == val and da[2][2] == val and da[3][2] == val:
            print(val + ' is the winner! ')
            sys.exit()            
        elif da[1][3] == val and da[2][3] == val and da[3][3] == val:
            print(val + ' is the winner! ')
            sys.exit()


def show():
    print('  ' + da[1][1] + ' || ' + da[1][2] + ' || ' + da[1][3] )
    print('================' )
    print('  ' + da[2][1] + ' || ' + da[2][2] + ' || ' + da[2][3] )
    print('================' )
    print('  ' + da[3][1] + ' || ' + da[3][2] + ' || ' + da[3][3] )
    print()


def user_xy(var):
    global varx
    global vary

    varx = var[0]
    vary = var[1] 

def user_out(c,y):
    da[c][y] = 'x'



da = {
    1:{1:' ', 2:' ', 3:' '},
    2:{1:' ', 2:' ', 3:' '},
    3:{1:' ', 2:' ', 3:' '}
}

while True:
    print('Enter a value: ')
    off = input()
    user_xy(off)
    user_out(int(varx),int(vary))
    com_xy()
    com_out(comx,comy)
    show()
    winner()
