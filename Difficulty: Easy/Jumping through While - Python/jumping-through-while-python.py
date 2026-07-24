def printIncreasingPower(x):
    i=1
    # Loop to jump in powers of 2
    while(i<=x):
        c=i*i
        if(c<=x):
            print (c , end = " ")
        
        i+=1