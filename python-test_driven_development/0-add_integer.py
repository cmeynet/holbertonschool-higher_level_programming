#!/usr/bin/python3
"""
This is the "0-add_integer" module
It coutains the function:
add_integer
"""


def add_integer(a, b=98):
    """ Addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
