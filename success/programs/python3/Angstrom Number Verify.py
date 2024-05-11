#Angstrom number : 153=1^3+5^3+3^3
#Other numbers : 153,370,371,407
import math

number = input("Enter the number : ")
x = number
y = len(x)
z  = float(x)
d = z
a = 0
for i in range(0,y):
 b = int(d% 10)

 c = b**3

 d = int((d-b)/10)
 a += c
 # print(d,b)
# a = int(a)
if a==z :
 print(x,"is an Angstrom number")
else :
 print(x,"is not an Angstrom number")