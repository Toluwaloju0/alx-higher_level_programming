#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    update_dictionary - to add a value to a dictionary
    a_dictionary: dictionary to be affected
    key: argument will be always a string
    value: argument of any type to be added
    """

    if a_dictionary is None:
        return None
    for i in a_dictionary:
        if i == key:
            a_dictionary[i] = value
            return a_dictionary
        continue
    a_dictionary[key] = value
    return a_dictionary
