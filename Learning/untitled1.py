# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:59:19 2020

@author: Foderking
"""
from fractions import Fraction

lst = [(1, 8), (1, 90), (1, 4)]
num = []
den = []
nden = []
none = []
prime = []
nnum = []
hcf = 1


for values in lst:                            # Get numerators and denumerators
    den.append(values[-1])
    num.append(values[0])   
for base in den:                              # Get Highest common factor
    hcf *= base 

        
nden = min(prime)                               # New denominator 
print(nden)
nnum = [ int(nden / den[x])for x in range(len(num)) ]

print(nnum)