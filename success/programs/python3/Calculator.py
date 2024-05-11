#Calculator
import math
x = float(input("Enter first number = "))
y = float(input("Enter second number = "))
z = input("Enter the operator : +,-,/,* : ")
a = x+y
absolute = math.sqrt(((x-y)**2))
s = (x-y)
m = x*y
d = (x/y)
if z == '+':
	print("Addition is = ",a)
	pass
elif z == '-':
	print("Substraction is = ",s)
elif z == '/':
	print("Division is = ",d)
elif z=='*':
	print("Multiplication is = ",m)
else :
	print("Wrong input")