#Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
def func(n):
    if n<1:
        return 0
    count=0
    while n!=1:
        if n%2==0:
            n=int(n/2)
            count+=1
        else:
            n=int(3*n+1)
            count+=1
    print(count)

func(12)