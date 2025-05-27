#!/usr/bin/python3
"""
This is the "10-square" modulo.
Its contains the class:
BaseGeometry
Rectangle
Square
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

    Methods:
        area: calculate area of the rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    Defines a Square depend of Rectangle

    Attributs:
        size: size of the square

    Methods:
        area: calculate area of the square
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
