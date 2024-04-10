#!/usr/bin/python3
"""A module to define a class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class called Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """A function to initialize a square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """To get a string of the class"""

        a = "[Square] ({}) ".format(self.id)
        b = "{}/{} - {}".format(self.x, self.y, self.width)
        return a + b

    @property
    def size(self):
        """To get the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """To set the value of size"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value

    def update(self, *args, **kwargs):
        """To update a xss instance"""

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
            self.height = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

    def to_dictionary(self):
        """To retrurn a dictionary of the class"""

        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.width
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
