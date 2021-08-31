import random, sys

def show():
    print('  ' + da[1][1] + ' || ' + da[1][2] + ' || ' + da[1][3] )
    print('================' )
    print('  ' + da[2][1] + ' || ' + da[2][2] + ' || ' + da[2][3] )
    print('================' )
    print('  ' + da[3][1] + ' || ' + da[3][2] + ' || ' + da[3][3] )
    print()

def user_out(c,y):


    da[c][y] = 'x'
    temp = str(c) + str(y)
    User.append(temp)

def com_out(c,y):

    da[c][y ] = '0'
    temp = str(c) + str(y)
    Com.append(temp)

def user_xy(var):
    global varx
    global vary

    varx = var[0]
    vary = var[1] 
def stale():
    if len(User) == 4 and len(Com) == 4:
        print('Stalemate!')
        sys.exit()

# def com_xy():
#     global comx
#     global comy
#     if da == {
#     1:{1:'x', 2:' ', 3:' '},
#     2:{1:' ', 2:' ', 3:' '},
#     3:{1:' ', 2:' ', 3:' '}
#             }:
#         comx = 2
#         comy = 2

#     elif da == {
#     1:{1:'x', 2:' ', 3:' '},
#     2:{1:' ', 2:'0', 3:' '},
#     3:{1:' ', 2:' ', 3:' '}
#             }:
#         comx = 2
#         comy = 2


def com_xy():
    global comx
    global comy

    while True:

        x = random.randint(1,3)
        y = random.randint(1,3)
        temp = str(x)+ str(y)

        if (   not(temp in User) and not(temp in Com)  ) :
            comx = x
            comy = y
            break

        else:
            continue

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

###################################
da = {
    1:{1:' ', 2:' ', 3:' '},
    2:{1:' ', 2:' ', 3:' '},
    3:{1:' ', 2:' ', 3:' '}
}
Com = []
User = []

show()
print('Welcome to hex and hoe ', end='')
while True:
    print('Enter a value: ')
    off = input()
    if str(off) in User or str(off) in Com:
        print('Error: value already exists!')
        continue
    else:
        try:
            user_xy(off)
            user_out(int(varx),int(vary))
        except (ValueError, IndexError, KeyError) :
            print('Error: Type in 2 numbers between 1-3!')
            continue
        com_xy()
        com_out(comx,comy)
        show()
        stale()
        winner()
        # print(Com)
        # print(User)
        # print(len(Com))
        # print(len(User))