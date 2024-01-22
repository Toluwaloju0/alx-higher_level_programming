#!/usr/bin/python3
"""A module that appends a text to a file"""


def append_write(filename="", text=""):
    """To append a text to a file
    Args:
        filename (string): the name of the file
        text (string) the text to be written
    """

    with open(filename, mode="a", encoding="utf-8") as a:
        a.write(text)
    return len(text)
