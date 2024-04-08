#!/usr/bin/python3
"""A module to create a function"""


def add_attribute(a_class, class_attr, class_value):
    """A finction to add a new attribute to the class"""

    if not hasattr(a_class, class_attr):
        setattr(a_class, class_attr, class_value)
    else:
        raise TypeError("can't add new attribute")
