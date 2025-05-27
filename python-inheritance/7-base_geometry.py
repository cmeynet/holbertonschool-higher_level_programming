#!/usr/bin/python3
"""
This is the "7-base_geometry" modulo.
Its contains the class:
BaseGeometry
"""


class BaseGeometry:
    """
    Defines a BaseGeometry

    Methods:
        area: calculate the area
        integer_validator: validate value
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
