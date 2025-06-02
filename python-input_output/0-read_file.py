#!/usr/bin/python3
""" It contains the function:
    read_file """


def read_file(filename=""):
    """ Function that reads a text file and prints it to stdout """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
