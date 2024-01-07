#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return None
    try:
        a, b = 0, 0
        for a in range(x):
            if type(my_list[a]) != int:
                continue
            print("{:d}".format(my_list[a]), end="")
            b += 1
        print("")
    except IndexError:
        raise
    return b
