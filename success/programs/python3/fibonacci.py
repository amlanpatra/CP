#Fibonacci series

def fib():
 x = int(input("Enter the limit : "))
 a = 0
 b = 1
 c = 1
 d = [1]
    
    
 for i in range (x):
       d.append(c)
       a=b
       b=c
       c=a+b
       
       
 print(d)
                
fib()       