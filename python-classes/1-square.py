#!/usr/bin/python3
""" Definition of a Square class with a private attribute """


class Square:
    """
    Defines a square

    Attributs :
        size: size of the square
    """

    def __init__(self, size):
        """
        Initialize a sqaure with new size

        Args:
            size: size of the square
        """
        self.__size = size
