def print_table(inp):
    i = 0
    j = 0
    while True:
        if j < 4 and i < 3:
            strin = inp[i][j]
            print(strin.rjust(coda[i]),end='| ')
            i += 1
        elif i > 2:
            i = 0
            j += 1    
            print()
        else:
            break

def col(va):
    global lag_col
    lag_col = 0
    for c in va:
        if len(c) > lag_col:
            lag_col = len(c)

def somth(data):
    for x in data:
        col(x)
        coda.append(lag_col)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alkkkkkkkkkkkkice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goooooooooose']]

coda = []

somth(tableData)
print_table(tableData)