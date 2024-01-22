#!/usr/bin/python3
"""A module to write a file"""


def write_file(filename="", text=""):
    """To write a text to a file
    Args:
        filename (string): the files name
        text (string): the text to be written
    """

    with open(filename, mode="w", encoding="utf-8") as a:
        a.write(text)
    return len(text)
