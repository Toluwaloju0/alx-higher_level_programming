#!/usr/bin/python3
"""A module that defines a function that prints a class dict
"""


def lookup(obj):
    """To print in a list the dict of obj
    Args:
        obj (class): A class
    """

    return list(obj.__dict__)
