#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return None
    try:
        a = 0
        for b in my_list:
            if a == x:
                break
            print(b, end="")
            a += 1
        print("")
    except IndexError:
        raise
    return a
