#!/usr/bin/python3
"""To change a json string to an object"""


def from_json_string(my_str):
    """A function to change a json string to a string
    Args:
        my_str (json string): the string
    """

    from json import loads

    return loads(my_str)
