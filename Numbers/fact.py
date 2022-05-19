def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)

print(fact(4))

def fact_loop(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

fact_loop(4)

