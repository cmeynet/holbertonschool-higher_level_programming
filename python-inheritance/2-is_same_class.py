#!/usr/bin/python3
"""
This is the "2-is_same_class" modulo.
Its contains the function:
is_same_class
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object
    is exactly an instance of a specified class
    """
    if type(obj) is a_class:
        return True
    return False
