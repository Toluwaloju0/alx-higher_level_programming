#!/usr/bin/python3
"""To define a class and assign it initial values
"""


class Square:
    """A class of a square
    """
    def __init__(self, value):
        """The initial values of the class
        Args:
            value (int): the size of the square
        """
        self.__size = value
