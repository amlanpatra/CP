# Python program to display calendar of 
# given month of the year
import os
print(os.getcwd())
import calendar 
    
yy = 2020
mm = 1

print(calendar.month(yy,mm))
print ("The calender of year 2020 is : ") 
print (calendar.calendar(2020, 2, 1, 6))