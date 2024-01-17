#!/usr/bin/python3
"""A module that makes a class"""


class Rectangle:
    """An empty classs
    """
    def __init__(self, width=0, height=0):
        """To initialize the attributes of the rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """To return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set the width to a value
        Args:
            value (int): the width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """To set the height to value
        Args:
            value (int): the height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """To find the area of the square
        """
        return self.__width * self.__height

    def perimeter(self):
        """To find the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))
