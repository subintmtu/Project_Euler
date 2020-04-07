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
                        FactorList[n] = 1
                        n = 1
                        break
                        
    return(pd.DataFrame.from_dict(FactorList, orient='index', columns=['Count']))

# *******************************************************************
# Check for Palindrome 

def isPalindrome(num):
    return(str(num)==str(num)[::-1])