#!/usr/bin/python3
""" Definition of a Square class with type vchecking """


class Square:
    """
    Defines a square

    Attributs :
        size (int): size of the square
    """

    def __init__(self, size=0):
        """
        Initialize a square with a size as an int

        Args:
            size (int): size of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
