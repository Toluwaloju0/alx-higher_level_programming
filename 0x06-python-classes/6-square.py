#!/usr/bin/python3
"""To set the position where a square os to be printed
"""


class Square:
    """A class of squares
    """
    def __init__(self, size=0, position=(0, 0)):
        """he initial values of the class
        Args:
            value (int): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance((value[0]), int) or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """to print the square using #
        """
        s = " "
        if self.__size == 0 or self.__position[0] == 0:
            print("")
        for a in range(self.__size):
            if self.__position[1] > 0:
                s = "_"
            for b in range(self.__position[0]):
                print(s, end="")
            for b in range(self.__size):
                print("#", end="")
            print("")
        return ("")
