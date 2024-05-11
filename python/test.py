def rotate(n, k):
    if(k > 0):

        for i in range(k):

            n = str(n)
            l = len(str(n))
            p = n[l-1]
            n = str(n)
            n = str(p)+n

            n = int(n)
            n = int(n/10)

            print(f"{n}")
    elif(k < 0):
        k = -k
        for i in range(k):

            n = str(n)
            l = len(str(n))
            p = n[0]
            n = str(n)
            n = n+str(p)

            new = 0
            rnew = 0
            n = int(n)
            m = n
            i = 1
            while(n != 0):
                digit = n % 10
                n = int(n/10)
                if(i != l):
                    new = new*10+digit
            i = i+1
            new = int(new/10)
            i = 1
            while(new != 0):
                digit = new % 10
                new = int(new/10)
                if(i != l):
                    rnew = rnew*10+digit
            i = i+1
            n = rnew

            print(f"{rnew}")


m = int(input("enter the number only integers accepted"))
k = int(input("enter the number of rotations u want "))
rotate(m, k)
