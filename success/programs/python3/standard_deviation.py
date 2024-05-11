import math
a=[]
b=0
for i in range(5):
    print('Enter number : ')
    a.append(int(input()))
#adding the numbers and finding mean
for x in a:
    b+=x
b/=5
print(a,b)
#difference between mean and numbers and finding sq. root
for y in range(5):
    a[y]=a[y]-int(b)
    a[y]=(a[y])**2

print(a)
b=0
#adding the numbers
for p in range(5):
    b+=a[p]
print(b)
b/=5
print(b)

b = math.sqrt(b)
print(b)