#!/usr/bin/python3
"""A module that changes a json string to an object"""


def load_from_json_file(filename):
    """A function that changes a json string to an object
    Args:
        filename (file): the file holding the string
    """

    from json import loads

    with open(filename, mode="r", encoding="utf-8") as a:
        return loads(a.read())
