#!/usr/bin/python3
""" Definition of an empty Rectangle class. """


class Rectangle:
    """
    Defines a rectangle

    Attributs:
        width: width of the rectangle
        height: height of the rectangle

    Methods:
        area: calculate the area of the rectangle
        perimeter: calculate the perimeter of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with width and height

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
            for i in range(self.__height):
                # str() to convert print_symbol
                string += (str(self.print_symbol) * self.__width)
                if i != (self.__height - 1):
                    string += '\n'
            return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle ...")
        Rectangle.number_of_instances -= 1
