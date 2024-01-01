#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    multiply_by_2 - to multply the values of a dict by 2
    a_dictionary: the dict to be affected
    """

    if a_dictionary is None:
        return None
    new_dictionary = {}
    for i, j in a_dictionary.items():
        new_dictionary[i] = j * 2
    return new_dictionary
