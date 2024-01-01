#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    complex_delete - to delete keys havong a value
    a_dictionary: the dictionary to be affected
    value: the value to be deleted
    """

    if a_dictionary is None:
        return None
    dict_remove = []
    for a, b in a_dictionary.items():
        if b == value:
            dict_remove.append(a)
            continue
    for a in dict_remove:
        del a_dictionary[a]
    return a_dictionary
