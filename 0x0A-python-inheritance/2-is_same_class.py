#!/usr/bin/python3
"""A modue that checks the tyoe of a list"""


def is_same_class(obj, a_class):
    """A function that checks id an obj is of type class
    Args:
        obj (class object): The object to be checked
        a_class (class): the class
    """

    if type(obj) is a_class:
        return True
    else:
        return False
