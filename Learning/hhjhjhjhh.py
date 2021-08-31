import random


stri = 'aabb'
i = 0
val = ''

for i in range(len(stri)):
    si = list(stri)
    del si[i]
    val += stri[i]
    for asdf in range(len(si)*len(si)):
        val += si[random.randit(len(si))]
        print(set(val))
 #   print(val)
    val = ''