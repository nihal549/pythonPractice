def sqSum(n):
    sq=0
    while n>=1:
        r =n%10
        sq =sq+r*r
        n=int(n/10)
    return sq
count=0
n=int(input('enter a number : '))
temp=n
while n>=1:
    n=sqSum(n)
    count+=1
    if(n==1):
       break
    elif count==10:
        break
    
if(n==1):   
    print(str(temp)+" is a happy number")
else:
    print(str(temp)+" is not a happy number")