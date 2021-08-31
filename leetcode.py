# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 01:49:54 2020

@author: Foderking
"""
import copy

d = []

dd = []
for j in range(3):
    dd.append(1)
    for i in range(len(d)):
        try:
            dd.append(d[i] + d[i + 1])
        except IndexError:
            dd.append(1)
            d = copy.copy(dd)
            print(d)
            break
