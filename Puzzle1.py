import sys

def prime(n):
    print(n)
    for i in range(2,n,1):
        if n % i == 0:
            return 0
    return 1

def main():
    inN = int(input("Input number:"))
    for max in range(inN,1,-1):
        if inN % max == 0:
            if prime(max) == 1:
                print(max)
                break

if __name__=="__main__":
    main()



