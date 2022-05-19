#Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
import math
def primeFactor(n):
    while n%2==0:
        print(2)
        n=n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            print(i)
            n=n/i

# n =int(input('enter number : '))
# primeFactor(n)

#Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
def isPrime(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                break
            else:
                print(n)
def nextPrime():
    n=3
    
    while True:
        choice=input("enter next or stop  :  ")
        if choice =="next":
            n=n+1
            isPrime(n)
        else:
            break
    
nextPrime()