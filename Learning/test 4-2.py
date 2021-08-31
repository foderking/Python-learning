grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


x = len(grid)
y = len(grid[0])
ix = 0
iy = 0
while True:
    for ix in range(x):
        print(grid[ix][iy],end='')
    print()
    iy += 1
    if not(iy < y and ix < x):
        ix,iy = 0,0
        break
print('BASED VERSION 1!')
print()
while True:
    print(grid[ix][iy],end='')
    ix += 1
    if not ix < x:
        ix = 0
        iy += 1
        print()
    if not(iy < y and ix < x):
        break    
print('BASED VERSION 2!')























































































########I.T.K 
# I KNOW