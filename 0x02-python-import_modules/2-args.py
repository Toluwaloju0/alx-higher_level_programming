#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{} argument.".format(len(argv) - 1))
        exit(0)
    else:
        print("{} argument:".format(len(argv) - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
        i += 1
