#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = 0
    for a in my_list:
        if a > i:
            i = a
    return i
