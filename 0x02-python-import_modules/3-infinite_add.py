#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0")
        exit()
    sum = 0
    for i in range(1, len(argv)):
        sum = sum + int(argv[i])
    print("{}".format(sum))
    exit()
