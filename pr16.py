# Write a password generator in Python.

import random
import string

def genPWD(ranStr,size = 8):
    return ''.join( random.choice(ranStr) for _ in range(size))

size = int(input("How long you need your password? "))
ranStr = string.ascii_letters + string.digits + ''.join(random.sample(string.punctuation,5))
print(ranStr)
print("Your password is : ", genPWD(ranStr,size))
