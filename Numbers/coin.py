import random
list =['head','tail']
n =int(input('how many times to flip coin..?'   ))
head =0
tail =0
for i in range(0,n):
     res=random.choice(list)
     if res=='head':
          head=head+1
     else:
          tail=tail+1

print('heads : ',head)
print('tails : ',tail)

     
    


