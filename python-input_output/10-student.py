#!/usr/bin/python3
""" It contains the class:
    Student """


class Student:
    """ Defines a Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        # Checks that each element in the list is a string (str)
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            """ retrieve the value of the corresponding attribute
            and only include the attributes that exist in the object."""
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
