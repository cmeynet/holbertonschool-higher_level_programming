#!/usr/bin/python3
"""
This is the "8-rectangle" modulo.
Its contains the class:
BaseGeometry
Rectangle
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


class Rectangle(BaseGeometry):
    """
    Defines a Rectangle depend of BaseGeometry

    Attributs:
        width: width of the rectangle
        height: height of the rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
