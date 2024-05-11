# List overlap comprehensions
import random
a = range(0,random.randint(0,50))
b = range(random.randint(20,30),random.randint(30,80))
print (a,b)
c = [for x in a for y in b if x==y]