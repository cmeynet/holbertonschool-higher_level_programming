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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with a size as an int

        Args:
            size (int): size of the square
            position: position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Getter to access the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter to modify position with verification """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculate the area of the current square

        Returns:
            The area of the current square
        """
        return self.__size * self.__size

    def my_print(self):
        """ Prints the square with the character # """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
