#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = [0] * (len(my_list) - 1)
    a = 0
    for i in range(len(my_list)):
        if i == idx:
            continue
        new_list[a] = my_list[i]
        a += 1
    new_list = my_list
    return new_list
