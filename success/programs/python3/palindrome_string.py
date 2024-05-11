# (A palindrome is a string that reads the same forwards and backwards.)
a = input("Give me any input : ")
if a == a[::-1]:
    print("{} is Palindrome".format(a))
else:
     print("{} is not Palindrome".format(a))
   


        