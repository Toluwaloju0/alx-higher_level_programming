#!/usr/bin/python3
"""A module to print a file"""


def read_file(filename=""):
    """A function that reads from filename and prints it
    Args:
        filename (string): the name of the file
    """

    with open(filename, mode='r', encoding="utf-8") as a:

        print(a.read(), end="")
