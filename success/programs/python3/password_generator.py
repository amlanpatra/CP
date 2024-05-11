import random
import pyperclip

def password(length=10, chars=1, spcl=1, num=1):
    def generator(chars, spcl, num):
        charset = random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") if chars == 1 else ''
        spclset = random.choice(
            "-") if spcl == 1 else ''
        # spclset = random.choice(
        #     "!@#$%^&*()_+}{[]|:;?/>.<,") if spcl == 1 else ''
        numset = random.choice("0123456789") if num == 1 else ''
        a = charset + spclset + numset
        return random.choice(a) if a != '' else ''
    pwd = ''
    for i in range(length):
        pwd += generator(chars, spcl, num)
    pyperclip.copy(pwd)
    print("Your password is {}".format(pwd))
    return pwd


# order : pwd length, char, spcl cahr, num
pwd = password(10, 1, 1, 1)


