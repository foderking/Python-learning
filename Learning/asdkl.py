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

def eval_(op1, oper, op2, get_operator_fn=ops.get):
    op1, op2 = float(op1), float(op2)
    return get_operator_fn(oper)(op1, op2)

op = ('/','*','+','-')

st = '3 / ( 4 - 10 ) * 2'
sa  = st.split()

def bodmas(s):
    while True:
        for o in op:
            while o in s: 
                n = s.index(o) - 1
 #               if s[i] == o:
                print(s)
          #      n = i-1
                if ( o == '/'or o == '*') and s[n-1] == '-':
               #     pre = [str(float(s[n])* -1)] + s[n+1:n+3]
                    print(pre)
             #   else:
                pre = s[n:n+3]
                new = eval_(*(pre))
                del s[n:n+3]
                s.insert(n,str(new))
             #   i -= 1
                print()

        if len(s) == 1:
            break
    return s
    
def solve(a):
    match = reg.search(' '.join(a))
    if match:
        catch  = match.group()[2:-2].split()
        solve(catch)
    return bodmas(a)
    
print(solve(sa))
#print(eval_(*("1 + 993".split())))