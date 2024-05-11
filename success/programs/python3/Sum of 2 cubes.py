# Sum of cube of 2 numbers
x = int(input("Enter the number = "))
y1 = int(float(x/3))
y2 = int(float(x/30))
y3 = int(float(x/100))
a = 0
b = (x-a)
for i in range(0,x):
  a+=1
  b=(x-a)
  cube1 = a**3
  for i in range(0,x):
   p=cube1+(b**3)
   print(p,a,b)
   if p==x :
    print("The numbers are =",a,"and",b)
    exit()
   else:
    if(b>0):
    	b-=1
    else:
     pass