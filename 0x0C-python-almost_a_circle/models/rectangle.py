#!/usr/bin/python3
"""A module to create a new class"""


from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """A function to initialize the class"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """A getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """A getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter methpod for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """a getter methid for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """A setter method for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """A getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """A setter method for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """To return the area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """To print the rectangle to stdout"""

        for a in range(self.y):
            print("")
        for a in range(self.height):
            for b in range(self.x):
                print(' ', end="")
            for b in range(self.width):
                print('#', end="")
            print("")

    def __str__(self):
        """To return a strin of rectangle"""

        a = "[Rectangle] ({}) ".format(self.id)
        b = "{}/{} - {}/{}".format(self.x, self.y, self.width, self.height)
        return a + b

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
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def to_dictionary(self):
        """To retrurn a dictionary of the class"""

        return self.__dict__
