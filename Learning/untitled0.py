def isPP(n):
    from math import log
    import random
    ns = []
    prime = []
    

    
    for var in range(2, n):
 #       var = random.randrange(2,n)
        print(var)
        if ( log(n,10)/log(var,10) ) == int( log(n,10)/log(var,10) ):
            ns.append(var)
            ns.append(int(log(n,10)/log(var,10)))
            return ns
    return
        
    
    
print(isPP(13462))