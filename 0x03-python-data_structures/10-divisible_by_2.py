#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    new_list = [0] * len(my_list)
    i = 0
    for a in my_list:
        if (a % 2) == 0:
            new_list[i] = True
        else:
            new_list[i] = False
        i = i + 1
    return new_list
