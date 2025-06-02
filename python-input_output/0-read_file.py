#!/usr/bin/python3
""" Function that reads a text file and prints it to stdout """


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
