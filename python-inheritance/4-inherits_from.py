#!/usr/bin/python3
"""
This is the "4-inherits_from" modulo.
Its contains the function:
inherits_from
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class.
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
