# List overlap comprehensions
import random
a = range(0,random.randint(10,50))
b = range(random.randint(20,30),random.randint(31,80))
c=[]
#print(a,b)
for x in a:
   if a[x] in b:
     c.append(x)    
print ("A is :",a,"\nB is :",b,"\nC is :",c)
