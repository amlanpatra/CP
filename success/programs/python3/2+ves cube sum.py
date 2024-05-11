#Sum of Cube Of 2 Positive numbers
x = int(input("Enter the number : "))
y = x
def sum():
 a=0
 b = (y-a)
 for i in range(0,y):
  a+=1
  b=(y-a)
  cube1 = a**3
  for i in range(0,y):
   p=cube1+(b**3)
   #print(p,a,b)
   if p==x :
    print("The numbers are =",a,"and",b)
    exit()
   else:
    if(b>0):
    	b-=1
    else:
     pass
if(x<10000):
 sum()
elif (x<50000) and (x>=10000):
 y = int(float(x/3))
 sum()
elif (x<500000) and (x>=50000):
 y = int(float(x/100))
 sum()
elif (x<5000000) and (x>=500000):
 y = int(float(x/1000))
 sum()
elif(x<=500000000) and (x<=5000000):
 y = int(float(x/10000))
 sum()
else :
 y = int(float(x/100000))
 sum()