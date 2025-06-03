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
        """ Retrieves a dictionary representation of a Student instance """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        # Iterate through each key-value pair in the json dictionary
        for key, value in json.items():
            # Assigns to the self object an attribute named key with the value value
            setattr(self, key, value)
