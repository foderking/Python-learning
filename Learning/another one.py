def user_xy(var):
    global varx
    global vary

    varx = var[0]
    vary = var[1] 

ja = {}
while True:
    op = input()
    if op == '':
        break
    user_xy(op)
    ja.setdefault(varx,{})
    ja[varx][vary] = ''
    print(ja)


for f, a in ja.items():
    for fd, ds in a.items():
        print(f,end='')
        print(fd)