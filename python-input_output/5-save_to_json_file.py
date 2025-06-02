#!/usr/bin/python3
""" It contains the function:
    save_to_json_string """
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation.
    """
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
