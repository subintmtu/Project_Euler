import math
import pandas as pd

# Returns true if the input n is prime
def isPrime(n) :
    """
    Returns true if the input n is prime
    """
    if (n == 2 or n == 3 ) : return (True)
    if n < 2 : return (False)
    if n%2 == 0 : return (False)
    if n < 9 : return (True)
    if n%3 == 0 : return(False)
    mxRange = int(math.sqrt(n))
    divisor = 5
    while divisor <= mxRange :
        if n%divisor == 0 : return (False)
        if n%(divisor+2) == 0 : return (False)
        divisor += 6
    return (True)

# *******************************************************************
# Returns prime factors and their count
def primeFactors(n):
    """
    Returns prime factors and their count
    """
    FactorList = {}

    if(isPrime(n)):
        FactorList[n] = 1
    else :
       
        counter = 0
        while(n%2==0):
            n = n//2
            counter = counter + 1
            FactorList[2] = counter
            
        if(isPrime(n)):
            FactorList[n] = 1
            n = 1
        
        maxRange = int(math.sqrt(n)) + 4
        if(maxRange%2==0): maxRange = maxRange + 5

        while (n!=1) :
            x, maxRange = maxRange - 2, maxRange - 2
            
            if(isPrime(x)):
                counter = 0
                while(n%x==0) :
                    n = n//x
                    counter = counter + 1
                    FactorList[x] = counter
                    if(isPrime(n)) :
                        if(n in FactorList.keys()):
                            FactorList[n] = FactorList[n] + 1
                        else:
                            FactorList[n] = 1
                        n = 1
                        break
                        
    return(pd.DataFrame.from_dict(FactorList, orient='index', columns=['Count']))

# *******************************************************************
# Check for Palindrome 

def isPalindrome(num):
    """
    Check Palindrome or not
    """
    return(str(num)==str(num)[::-1])

# *******************************************************************
# Generate Palindrome

def genPalindrome(num = 1000):
    """
    Returns a series of palindromic numbers with same number of digits 
    less than or equal to num
    """
    digLen = len(str(num))
    pal = []
    if(digLen%2):
        Len = (digLen-1)//2
        na = int(num)//10**(Len)
        LLim = 10**(Len) - 1
        npal = int(str(na) + str(na)[-2::-1])
        if(npal > num):
            na = na - 1
        for i in range(na,LLim,-1):
            npal = int(str(i) + str(i)[-2::-1])
            pal.append(npal)
    else:
        Len =  digLen//2
        na = int(num)//10**(Len)
        LLim = 10**(Len-1) - 1
        npal = int(str(na) + str(na)[::-1])
        if(npal > num):
            na = na - 1
        for i in range(na,LLim,-1):
            npal = int(str(i) + str(i)[::-1])
            pal.append(npal)
    return(pd.Series(pal))