stri = 'aabb'
i = 0
val = ''

for i in range(len(stri)):
    si = list(stri)
    del si[i]
    val += stri[i]
    for ea in si:
        val += ea
    print(val)