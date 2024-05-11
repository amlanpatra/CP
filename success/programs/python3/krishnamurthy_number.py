# Krishnamurthy number : Sum of factorial of the digits is equal to the number
import math
import datetime
a=[]
d=1
n = datetime.datetime.now()
limit = input("Enter the limit : ")
limit_len = int(limit)
x= n.timestamp()
#print('\n',x)
for i in range (1,limit_len+2):
    g = i
    c = len(str(i))
    f=0

    for p in range(0,c):
        d = g%10
        e = math.factorial(d)
        g = (g-d)//10
        f += int(e)        
    g=i  
    
    if (f==g):
      a.append(f)
n = datetime.datetime.now()
y = n.timestamp()
#print('\n',y)
print('\n',a)
print('time required : ', y-x)