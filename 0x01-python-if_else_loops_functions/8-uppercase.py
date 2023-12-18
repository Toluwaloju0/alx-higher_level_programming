#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) >= 97) and (ord(str[i]) <= 122):
            x = ord(str[i]) - 32
        else:
            x = ord(str[i])
        print("{:c}".format(x), end="")
    print("".format())
