#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    uniq_add - to add all unique elements in a list
    my_list: the list to be affected
    """
    if my_list is None:
        return None
    new_list = set(my_list)
    add = 0

    for a in new_list:
        add = add + a
    return add
