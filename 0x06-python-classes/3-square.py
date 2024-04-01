#!/usr/bin/python3
"""To make a method that finds the value of the area of the square
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

    def area(self):
        """The area of the square
        """
        return self.__size ** 2
