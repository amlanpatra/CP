# Write a program (function!) that takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates.

import random
a = []
b = ['henry','rocky','mini','bob','jason','john',14,4,5,7,5,25,12,14,14,12,16,17,17,18,2,94,94,67,5,166]
for i in range(30):
    a.append(random.randint(0,200))
c = list(set((list(set(a)))+list(set(b))))
print(c)