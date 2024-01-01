#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    print_sorted_dictionary - to print a dict in sorted manner
    a_dictionary: the affected dict
    """

    if a_dictionary is None:
        return None
    for a, b in sorted(a_dictionary.items()):
        print("{:s}:".format(a), b)
