#fabonaci
def fabonaci(n):
    if n<0:
        print('wrong input..')
    n1=0
    n2=1
    count =0
    if n==1:
        print(n1)
    else:
        while count<n:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1

#fabonaci(9)

#fabonaci recursion
def fabrec(n):
    if n<0:
        print("wrong input")
    elif n ==1 or n==2:
        return 1
    else:
        return fabrec(n-1)+fabrec(n-2)

print(fabrec(9))

