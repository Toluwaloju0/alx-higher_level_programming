#!/usr/bin/python3
"""A module to print a name"""


def say_my_name(first_name="", last_name=""):
    """A function that print a string
    Args:
        first_name (str): the first name of the object
        last_name (str): the last name of the object
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if first_name is None and last_name is None:
        print("My name is")
        return None
    print("My name is {} {}".format(first_name, last_name))
