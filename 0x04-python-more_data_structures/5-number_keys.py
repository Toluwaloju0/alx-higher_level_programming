#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    number_keys - to return the number of keys in a dict
    a_dictionary: the dictionary given
    """

    if a_dictionary is None:
        return None
    i = 0
    for a in a_dictionary:
        i += 1
    return i
