# machine guesses a random number and user guesses it
import random
a = random.randint(0,10)
b= int(input("User enter a number between 0-10 : "))
if a==b:
    print("Machine selected : ",a,"\nHooray, right match")
else:
    print("Machine selected",a,",better luch next time")