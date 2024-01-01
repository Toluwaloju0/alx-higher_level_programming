#!/usr/bin/python3
def highest_score(a_dictionary):
    """
    best_score - to find the best score in a dictionary
    a_dictionary: the dictionary to be affected
    """
    c = 0
    for a, b in a_dictionary.items():
        if b > c:
            c = b
    return c

def best_score(a_dictionary):
    """
    best_score - to find the best score in a dictionary
    a_dictionary: the dictionary to be affected
    """
    if a_dictionary is None:
        return None

    c = highest_score(a_dictionary)
    for a, b in a_dictionary.items():
        if b == c:
            return a
    return None
