#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
msg = "Last digit of "
six = "and is less than 6 and not 0"
if (((number % 10) > 5)):
    print(f"{msg}{number} is {(number % 10)} and is greater than 5")
elif (((number % 10) == 0)):
    print(f"{msg}{number} is {(number % 10)} and is 0")
else:
    if (number < 0):
        print(f"{msg}{number} is -{10 - (number % 10)} {six}")
    else:
        print(f"{msg}{number} is {(number % 10)} {six}")
