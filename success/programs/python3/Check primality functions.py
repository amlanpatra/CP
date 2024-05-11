#Exercise 11 : Check prime number
def pn():
 a=[]
 num=int(input("Enter a number : "))
 hf = (num//2 + 1)
 x = ("is not a prime number.")
 for i in range(1,hf+1):
     if num % i ==0:
         a.append(i)
 if max(a) > 1:
     print (num,"is not a prime number.\nThe divisors of",num," are :",a)
 else:
     print (num,"is a prime number.")
 
pn()