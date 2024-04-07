#!/usr/bin/python3
"""A module to check if a class inherits fromm another class"""


def inherits_from(obj, a_class):
    """A function to check if an object is a subclass of another
    Args:
        obj: The object to check
        a_class: the class to be tested against
    """

    if isinstance(obj, a_class):
         return True
    return False
