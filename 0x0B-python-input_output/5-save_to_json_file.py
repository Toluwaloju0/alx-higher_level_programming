#!/usr/bin/python3
"""A module that saves a json string in a file"""


def save_to_json_file(my_obj, filename):
    """A function that writes json(my_object) to a file
    Args:
        my_obj (object): the object to be used
        filename: the name of the file
    """

    from json import dumps

    with open(filename, mode="w", encoding="utf-8") as a:
        a.write(dumps(my_obj))
