import random
import string
 
def randString(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
 
for x in range(60000):
    firstname = randString()
    secondname = randString()
    print ("{} {}".format(firstname, secondname))