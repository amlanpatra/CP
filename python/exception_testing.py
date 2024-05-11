# a = 12
try:
    # if(a == 10):
    a = 5
    a = a/0
    # print("a is 10")

except Exception as e:
    print("error is : " + e.message)
