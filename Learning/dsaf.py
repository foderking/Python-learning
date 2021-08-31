from itertools import permutations
 
def longest_consec(strarr, k):
    str_len = len(strarr) - 1
    leng = 0
    perm = []
    srt =[]
    o, p, w = 0,1,2
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return 
    s = sorted(strarr, key=len, reverse = True)
    for f in range(k):
        leng += len(s[f])
    arr = list(permutations(strarr, k))
    for x in arr:
        perm.append(''.join(x))
    while True:
        if o > str_len :
            break
        elif p > str_len :
            p = 0 
        elif w > str_len :
            w = 0            
        srt.append(strarr[o] + strarr[p] + strarr[w])
        o += 1
        p += 1
        w += 1
        
    print(srt)
    print(leng)
    for ia in srt:
        if len(ia) == leng :
            print(ia)
        

longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"],2)