#Angstrom number : 153=1^3+5^3+3^3
#Other numbers : 153,370,371,407
#import math
#import timeit
#testing_code = """
ang_list = []
#number = input("Enter the range : ")
p = 1
#for the_range in range(0,int(number)):
for the_range in range(0,1000):
 x = str(p)
 y = len(x)
 z  = float(x)
 d = z
 a = 0
 for i in range(0,y):
  b = int(d % 10)
  c = b**3
  d = int((d-b)/10)
  a += c
#print (a)
# print(d,b)
# a = int(a)
 if a==p :
  ang_list.append(a)
  p+=1
  continue
 else :
  p+=1    
 continue
print(ang_list)
#"""
#time_to_perform = timeit.timeit(testing_code,number = 1)
#print (time_to_perform)

