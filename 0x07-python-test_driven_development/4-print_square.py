#!/usr/bin/python3
"""A module to print a square"""

def print_square(size):
    """A function to print a square
    Args:
        size(int): the size of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        return None
    for a in range(size):
        for b in range(size):
            print("#", end="")
        print ("")
