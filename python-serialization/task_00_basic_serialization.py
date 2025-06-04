#!/usr/bin/python3
""" It contains the function:
    serialize_and_save_to_file
    load_and_deserialize """
import json


def serialize_and_save_to_file(data, filename):
    """ Serialize and save data to a json file"""
    with open(filename, "w") as file:
        return json.dump(data, file)


def load_and_deserialize(filename):
    """ Load and deserialize data from a json file """
    with open(filename, "r") as file:
        return json.load(file)
