import sys
def Sexer(i):
    chas = 0
    i = int(i)
    while chas < i:
        print(chas)
        chas = chas + 1
while True:
    print('Input a number')
    ope = input()
    if ope == 'x':
        sys.exit()
    Sexer(ope)
