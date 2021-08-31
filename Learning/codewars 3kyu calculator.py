# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 08:44:08 2020
@author: Foderking
"""
import operator
import re

reg = re.compile(r'\(.*\)')
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}
op = ('/','*','+','-')
st =     "-7 * -(6 / 3)"
sa  = re.findall(r'(?:\d\.?)+|[*+/()-]', st)
# print(sa)

def eval_(op1, oper, op2, get_operator_fn=ops.get):     
    op1, op2 = float(op1), float(op2)
    return get_operator_fn(oper)(op1, op2)

def ddmass(s):
    while True:
        for o in op:
            while o in s: 
                # print(s)
                if len(s) == 2:
                    s = [s[0] + s[1]]
                    #print(s)
                    continue

                    
                n = s.index(o) - 1
                if s[n-1] == '-':
                    pre = [s[n-1] + s[n]] + s[n+1:n+3] 
         #           print(s[n+1:n+3])
                elif s[n+1] and s[n+2] in op:
                    pre = s[n:n+2]  +  [s[n+2]+ s[n+3]] 
                    del s[n+2]
                else:
                    pre = s[n:n+3]
                new = eval_(*(pre))
                # print(new)

                if s[n+1] and s[n+2] in op:
                    pass
                elif new < 0  and len(s)==3:
                    s[n-1]  = '-'
                elif new < 0:
                    s[n-1] = '-'
                    new *= -1
                elif new > 0 and s[n-1] == '-':
                    s[n-1] = '+'
 
                # print(s[n])
                del s[n:n+3]
                s.insert(n,str(new))
                
        if len(s) == 1:
            return float(s[0])
            break

def bodmas(s):
    while True:
        for o in op:
            while o in s: 
                if len(s) == 2:
                    s = [s[0] + s[1]]
                    #print(s)
                    continue
                n = s.index(o) - 1
              #  print(s)
                if s[n-1] == '-':
                    pre = [s[n-1] + s[n]] + s[n+1:n+3] 
         #           print(s[n+1:n+3])
                elif s[n+1] and s[n+2] in op:
                    pre = s[n:n+2]  +  [s[n+2]+ s[n+3]] 
                    del s[n+2]
                else:
                    pre = s[n:n+3]
                new = eval_(*(pre))
                # print(new)

                if s[n+1] and s[n+2] in op:
                    pass
                elif new < 0  and len(s)==3:
                    s[n-1]  = '-'
                elif new < 0:
                    s[n-1] = '-'
                    new *= -1
                elif new > 0 and s[n-1] == '-':
                    s[n-1] = '+'
 
                # print(s[n])
                del s[n:n+3]
                s.insert(n,str(new))
                
        if len(s) == 1:
            return s
            break
i,j = 0 ,0   
def solve(a):
    global i,j
    if a[0] == '-':
     #   print('faaaa')
        a[1] = a[0] + a[1]
        # print(s[1])
        del a[0]
        # print(s[0])
        # pre = a[n:n+3]    
    i +=1
    d = ' '.join(a)
    match = reg.search(d)
    if match:
        catch  = match.group()[2:-2].split()

        new = d[:match.start()].split()
        old = d[match.end():].split()
        j += 2
        return solve(new + solve(catch) + old)

    elif i - j == 1:
        return ddmass(a)
    else:
        # i -= 1
        return bodmas(a)
    
print(solve(sa))
# print(type(solve(sa)))
#print(j)
