def longest_consec(strarr, k):
    global c
    c = []           
  #  leng = 0
    n = len(strarr)
    i = 0
    lis = []
    
    if n == 0 or k > n or k <= 0:
        return "l"
    # s = sorted(strarr, key=len, reverse = True)
    # for f in range(k):
    #     leng += len(s[f])
        
    while True:
        if i == ( n - k ) + 1:
            break
        va = ''
        for x in range(k):
            va += strarr[i + x]
        lis.append(va)
        i += 1 

#    print(s)
 #   print(leng)
    return sorted(lis, key=len, reverse = True)[0]
    
print(  longest_consec(c, 2)   )