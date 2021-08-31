"""
pass in the expression and path you want to use in  the command line
command: python 'expression' 'path' 
"""

import os, re, sys
reg = re.compile(sys.argv[2])
# Gets path and navigates to it.
path = sys.argv[1]
os.chdir(path)
# Opens all txt files 
for i in os.listdir(path):
    if i.endswith('.txt'):
        # finds line that matches an expression.
        tx = open(os.path.join(path, i)).readlines()
        for j in tx:
            # print(j)
            if reg.search(j.lower()):
                print(f'line {tx.index(j)+ 1} in {os.path.join(path,i)}')

