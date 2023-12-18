#!/usr/bin/python3
x = 122
while x >= 97:
    if x % 2 == 1:
        x = x - 32
    print("{:c}".format(x), end="")
    if x < 96:
        x = x + 32
    x = x - 1
