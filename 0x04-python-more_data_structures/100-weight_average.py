#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    weight_average - to find the average of a tuple in a list
    my_list: the list to be affected
    """

    if my_list is None:
        return 0
    a = 0
    c = 0
    for b in my_list:
        c = c + (b[0] * b[1])
        a = a + b[1]
    return c / a
