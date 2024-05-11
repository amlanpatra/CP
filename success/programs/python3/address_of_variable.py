a = [10,11,12,13]
#print(a)
# There is nothing called NULL in Python.But there is "None"
B= hex(id(a))
c = a[:]
c.append(14)
#d = hex(id(c))
c = None
d = hex(id(c))
print(a,B,c,d)