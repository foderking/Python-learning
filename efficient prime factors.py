INPUT = 9


import math
from fractions import gcd    
data = {}

def primeFactors(n):       
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        data.setdefault(2,0)
        data[2] += 1
        n = n / 2          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2):           
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            data.setdefault(i,0)
            data[i] += 1            
            n = n / i               
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        data.setdefault(n,0)
        data[n] += 1           
    return data
    
A = list(primeFactors(INPUT).keys())
print(A)
for i in A:
    if (math.log(INPUT) / math.log(i)) == int(math.log(INPUT) / math.log(i)) :
        print(i)
        print((math.log(INPUT) / math.log(i)))