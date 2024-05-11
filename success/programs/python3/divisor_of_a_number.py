# Program to find out divisors of a number
x = float(str(input("enter the number : ")))
a = []
for i in range(2,int((x/2)+1)):
    if (float(x) % i == 0):
        a.append(i)
    else:
     continue
print (a)