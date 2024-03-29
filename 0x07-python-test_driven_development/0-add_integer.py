#!/usr/bin/python3
"""This is an addition module
"""
import doctest


def add_integer(a, b=98):
    """To add two integers
    Args:
        a (int): the first integer
        b (int):the second integer
    Returns the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
