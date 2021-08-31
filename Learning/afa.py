import operator
import re


reg = re.compile(r'\(.*\)')
sample = ' ( ( 2 ) * 3 )'.split()
def bod(f):
    return str(int(f[0]) + int(f[-1]))
    
def solve(a):
    #print(a)
    match = reg.search(' '.join(a))
    if match:
        catch  = match.group()[2:-2].split()
        print(catch)
        return solve(catch)
    else:
        return 'No'
    
print(solve(sample))
#print(eval_(*("1 + 993".split())))