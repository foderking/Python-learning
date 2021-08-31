import re 

def cc(va):
    return re.compile(r'\d\d\d-\d\d\d-\d\d\d\d').search(va)

print(cc(input()))
