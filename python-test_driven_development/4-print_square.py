#!/usr/bin/python3
"""
This is the "4-print_square" modulo.
It contains the function :
print_square
"""


def print_square(size):
    """"
    Prints a square with the character #

    parameter:
    size : The size of the square, must be an integer >= 0.

    return :
    None.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        print('#' * size)
