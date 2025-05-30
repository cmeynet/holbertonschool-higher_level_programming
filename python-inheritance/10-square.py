#!/usr/bin/python3
"""
This is the "10-square" modulo.
Its contains the class:
BaseGeometry
Rectangle
Square
"""
Rectangle = __import__("8-rectangle").Rectangle


class Square(Rectangle):
    """
    Defines a Square depend of Rectangle

    Attributs:
        size: size of the square

    Methods:
        area: calculate area of the square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
