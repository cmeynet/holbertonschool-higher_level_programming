#!/usr/bin/python3
""" It contains the function:
    append_write """


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file
    and returns the number of characters added.
    """
    with open(filename, "a") as file:
        return file.write(text)
