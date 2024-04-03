#!/usr/bin/python3
"""This is an addition module
"""


def add_integer(a, b=98):
    """To add two integers
    Args:
        a (int): the first integer
        b (int):the second integer
    Returns the addition of a and b
    """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(result)
