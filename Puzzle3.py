
import sys
from math import sqrt

def combin(n,r):
    if r == 1:
        return n
    elif n == r:
        return 1
    else:
        return combin(n-1,r) + combin(n-1,r-1)

def main():
    numN = int(input("Please Enter the number of n:"))
    numR = int(input("Please Enter the number of r:"))
    
    result = combin(numN, numR)

    print(result)
    return result

if __name__=="__main__":
    main()



