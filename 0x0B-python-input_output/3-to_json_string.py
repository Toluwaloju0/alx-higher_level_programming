#!/usr/bin/python3
"""A module to change an object to json mode"""


def to_json_string(my_obj):
    """function to change my_obj to json format
    Args:
        my_obj (object): the object to be changed
    """
    from json import dumps
    return dumps(my_obj)
