# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.

def lt():
    import random
    a=[]
    n=10
    for j in range(n):
     a.append(random.randint(1,100))

    b = a[::-1]
    print("The random list is:",a,"\nThe first and last numbers are :",a[0],b[0])
lt()