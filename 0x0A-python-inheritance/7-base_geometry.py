#!/usr/bin/python3
"""To create a class and dedine some methods"""


class BaseGeometry:
    """A class named basedgeometry"""

    def integer_validator(self, name="", value=0):
        if len(name) == 0:
            return None
        self.name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        self.value = value

    def area(self):
        """To find the area"""
        raise Exception("area() is not implemented")
