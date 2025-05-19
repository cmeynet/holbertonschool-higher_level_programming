#!/usr/bin/python3
""" Definition of a Square class with type checking
and method to calcul the area of the square and print it """


class Square:
    """
    Defines a square and calculate its area

    Attributs :
        size (int): size of the square

    Methods:
        area: calculate the area of the square
        my_print: print the square with #
    """
    def __init__(self, size=0):
        """
        Initialize a square with a size as an int

        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ Getter to access the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter to modify size with verification """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate the area of the current square

        Returns:
            The area of the current square
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
