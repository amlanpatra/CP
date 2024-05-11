import datetime
import calendar
now = datetime.datetime.now()

#print
print ("Current date and time using str method of datetime object:")
print (str(now))

#print
print ("Current date and time using instance attributes:")
print ("Current year: %d" % now.year)
print ("Current month: %d" % now.month)
print ("Current day: %d" % now.day)
print ("Current hour: %d" % now.hour)
print ("Current minute: %d" % now.minute)
print ("Current second: %d" % now.second)
print ("Current microsecond: %d" % now.microsecond)

#print
print ("Current date and time using strftime:")
print (now.strftime("%Y-%m-%d %H:%M"))

##print
print ("Current date and time using isoformat:")
print (now.isoformat())


a=str(format(now.hour))+":"+str(format(now.minute))
b=str(format(now.day))+" "+str(format(now.month))+" "+str(format(now.year))

c = datetime.datetime.strptime(b, '%d %m %Y').weekday() 
d=calendar.day_name[c]




print(a,b,c,d)

print ("Current hour: %d" % now.hour)