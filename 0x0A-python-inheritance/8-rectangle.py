#!/usr/bin/python3
"""A module to create a rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ A class to create  rectangle"""


    def __init__(self, width, height):
        """The initialization method
        Args:
            width(int): an integer to serve as the class width
            height(int): an integer to serve as the class height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
