import math
x = input("Enter the limit : ")
y = len(x)
z  = float(x)
d = z
a = 0
num = []
for i in range(0,x):
 for i in range(0,y):
  b = int(d% 10)

  c = math.factorial(b)

  d = int((d-b)/10)
 a += c
 # print(d,b)
# a = int(a)
     if a==z :
       num.append(z)
    else :
 #print("The sum of the factorial of the digits is",a,"instead of",x," so",x,"is not a Peterson number")
       print(x,"is not a Peterson number")
       
       
       
       '''import math
x = input("Enter the number : ")
y = len(x)
z  = float(x)
d = z
a = 0
l = list()
for i in range(0,y):
 b = int(d% 10)

 c = math.factorial(b)

 d = int((d-b)/10)
 a += c
 # print(d,b)
# a = int(a)
  l = l.append(a)
if a==z :
 print(l)
else :
 #print("The sum of the factorial of the digits is",a,"instead of",x," so",x,"is not a Peterson number")
 print(x,"is not a Peterson number")'''