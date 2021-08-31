import os, pprint
import numpy as np

f1 = open("C:\\Users\\Foderking\\Downloads\\al-m.txt")
f2 = open("C:\\Users\\Foderking\\Downloads\\missing.txt")
f3 = open("C:\\Users\\Foderking\\Downloads\\new.txt")

al = f1.readlines()
main = f2.readlines()
ne = f3.readlines()
new =  set(main) - set(ne)
print(len(new))
# pprint.pprint(sorted(new))
# d = open("C:\\Users\\Foderking\\Downloads\\missing.txt", 'w')
# d.write(''.join(list(new)))

