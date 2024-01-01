#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    simple_delete - to delete a key in a dictionary
    a_dictionary: the dictionary to be affected
    key: the key to be deleted
    """

    if a_dictionary is None:
        return None
    for i in a_dictionary:
        if i == key:
            del a_dictionary[i]
            return a_dictionary
        continue
    return a_dictionary
