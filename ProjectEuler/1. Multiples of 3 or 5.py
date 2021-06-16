class Divisibles:
    theSum=0
    for candidate in range(1000):
        if candidate%3==0 or candidate%5==0:
            theSum+=candidate
    
    print (theSum)
    