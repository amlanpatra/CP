# Reversing words

def rev_str():
    a = input()
    b = a.split()
    c = b[::-1]
    d = " ".join(c)
    print (d)
        
rev_str()