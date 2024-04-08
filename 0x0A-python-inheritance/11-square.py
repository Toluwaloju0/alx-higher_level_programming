#!/usr/bin/python3
"""A module to dedine a class square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from rectangle"""

    def __init__(self, size):
        """A function to initialize th xlass"""

        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """A module to show what to print"""

        return "[Square] {}/{}".format(self.__size, self.__size)
