#!/usr/bin/python3
"""To print a square
"""


class Square:
    """A class of squares
    """
    def __init__(self, size=0):
        """The initial values of the class
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

    def my_print(self):
        """to print the square using #
        """
        if self.__size == 0:
            print("")
        for a in range(self.__size):
            for b in range(self.__size):
                print("#", end="")
            print("")
        return ("")
