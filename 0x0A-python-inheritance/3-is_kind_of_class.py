#!/usr/bin/python3
"""To check the type of a class"""


def is_kind_of_class(obj, a_class):
    """A function to check the type of a class
    Args:
        obj (class): the object to be checked
        a_class (class): the class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
