#!/usr/bin/python3
""" Definition of a Square class with type checking
and method to calcul the area of the square  """


class Square:
    """
    Defines a square and calculate its area

    Attributs :
        size (int): size of the square

    Methods:
        area: calculate the area of the square
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

    def area(self):
        """ Calculate the area of the current square

        Returns:
            The area of the current square
        """
        return self.__size * self.__size
