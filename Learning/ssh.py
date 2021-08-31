dat = []
s = "pwwkew"
for i in range(len(s)):
    temp = []
    ii  = i 
    while True :
        if s[ii] == s[ii+1]:
            temp.append(s[ii])
            print('fffffffffffffffffffffffffffffffffffffffffff')
            break
        temp.append(s[ii])
        ii += 1
        print(temp)
    dat.append(temp)
print(dat)