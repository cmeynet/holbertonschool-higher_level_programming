#!/usr/bin/python3
"""
This is the "8-rectangle" modulo.
Its contains the class:
BaseGeometry
Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a Rectangle depend of BaseGeometry

    Attributs:
        width: width of the rectangle
        height: height of the rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
