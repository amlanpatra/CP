# Print even number in list
a = [1, 4,9, 16, 25, 36, 49, 64, 81, 100]
c=[]
p=0
for i in a :
    if (a[p]%2 == 0):
     c.append(a[p])
     p+=1
    else :
     p+=1
print(c)