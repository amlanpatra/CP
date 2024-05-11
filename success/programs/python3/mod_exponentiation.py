# 120! * 321! % 10^7 +9
import fileinput
for line in fileinput.input(files ='input.txt'): 
	a = str(line) 

def fact(x): 
	sum =1
	while(x>1):
		sum = sum*x
		x-=1
	return sum



def prod(p,q):		# p is dividend and q is divisor
	product = 1
	for x in range(2,p+1):
		product = product * (x % q)
	return (product % q)

import time
start =  time.clock()
#final = (prod(120, (10000000+9)) * prod(321,(10000000+9))) % (10000000+9)
final = (fact(120) * fact(321)) % (10000000+9)
print(final)
end = time.clock()
total = end - start
print("Total time : %.7f"%total)