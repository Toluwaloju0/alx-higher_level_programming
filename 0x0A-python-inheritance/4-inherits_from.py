#!/usr/bin/python3
"""A module to check if a class inherits fromm another class"""


def inherits_from(obj, a_class):
    """A function to xhexk if a class is a subclass of another
    Args:
        obj: The onject to check
        a_class: the class to be teste against
    """

    if obj.__class__ == a_class:
        return False
    for base_class in obj.__class__.__bases__:
        if inherits_from(base_class, a_class):
            return True
    return False
