def rotate(n, k):
    k %= len(str(n))
    print(int(str(n % (10**k)) + str(int(n/(10**k)))))


m = int(input("enter the number only integers accepted "))
k = int(input("enter the number of rotations u want "))
rotate(m, k)
