#!/usr/bin/python3
"""A module to define a class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class called Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """A function to initialize a square class"""

        super().__init__(size, size, x, y, id)
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size

    def __str__(self):
        """To get a string of the class"""

        a = "[Square] ({}) ".format(self.id)
        b = "{}/{} - {}".format(self.x, self.y, self.width)
        return a + b

    @property
    def size(self):
        """To get the value of size"""

        return self.__size

    @size.setter
    def size(self, value):
        """To set the value of size"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
