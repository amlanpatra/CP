x = int(input("Enter the year = "))
if (x % 100 == 0):
    if (x % 4 == 0) and (x % 400 == 0):
        print("Leap Year")
    else:
        print(x, "is not a leap year")
elif (x % 4 == 0):
    print("Leap Year")
else:
    print(x, "is not a Leap Year")
    