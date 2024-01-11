#!/usr/bin/python3
"""To define a class square and make it private values set to a value
"""


class Square:
    """A class of squares
    """
    def __init__(self, size=0):
        """he initial values of the class
        Args:
            value (int): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """to set the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """To set the value of the square
        args:
            value (int): the integer to be passed
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square
        """
        return self.__size ** 2
