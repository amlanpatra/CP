import sys
import fileinput 
for line in fileinput.input(files ='input.txt'): 
	a = str(line) 
sum = 0
for i in a:
	if(ord(i)!=47): 
		sum += int(i)
for x in range(2):	
	if(sum > 10):
		sum = sum%10 + (int(sum/10))%10
print("lucky number : "+str(sum))