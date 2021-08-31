import math
from fractions import gcd
data = {}

def primeFactors(n):       
    while n % 2 == 0: 
        data.setdefault(2,0)
        data[2] += 1
        n = n / 2          
    for i in range(3,int(math.sqrt(n))+1,2):           
        while n % i== 0: 
            data.setdefault(i,0)
            data[i] += 1            
            n = n / i               
    if n > 2: 
        data.setdefault(n,0)
        data[n] += 1           
    return data

def isPP(n):
    s = 1
    A = list(primeFactors(n).values())
    B = list(primeFactors(n).keys())
    res = A[0]
    for c in A[1::]:
        res = math.gcd(res , c)

    for i in B:
        if (math.log(n) / math.log(i)) !=1 and round(math.log(n) / math.log(i), 8) == int(math.log(n) / math.log(i)) :
            return [i, int(math.log(n) / math.log(i))] 
        elif (math.log(n) / math.log(i)) !=1 and A.count(A[0]) == len(A):
            for j in B:
                s *= j
            return [s, A[0]]
      #  else: 
    return None