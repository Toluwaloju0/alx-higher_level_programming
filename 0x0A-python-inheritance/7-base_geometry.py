#!/usr/bin/python3
"""To create an emoty class"""


class BaseGeometry:
    """A class named basedgeometry"""
    
    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        self.value = value

    def area(self):
        """To find the area"""
        raise Exception("area() is not implemented")
