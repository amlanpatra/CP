import random
a = range(1,random.randint(1,40))
b = range(1,random.randint(1,100))
c = []
print(a)
print(b)
for i in a:
    if i in b:
        c.append(i)
print(c)