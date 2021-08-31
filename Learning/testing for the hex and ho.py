first = {1:'a',2:'b',3:'c'}
second = {1:'q',2:'w',3:'e'}

import random

def user_xy(var):
    global varx
    global vary

    varx = var[0]
    vary = var[1] 

def asf(x, y):
    if (not(x in first.keys() and y in first.values()) and not(x in second.keys() and y in second.values()) ):
        print(x)
        print(y)
    else:
        print('no')


while True:
    print('enter a value: ')
    user_xy(input())
    zx = random.randint(1,3)
    asf(zx,vary)


