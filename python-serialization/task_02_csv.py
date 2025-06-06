#!/usr/bin/python3
""" It contains the function:
convert_csv_to_json"""
import csv
import json


def convert_csv_to_json(filename):
    """ Function that reading data from one format (CSV)
    and converting it into another format (JSON)"""

    json_file = 'data.json'
    try:
        with open(filename, "r") as file_csv:
            read_csv = csv.DictReader(file_csv)
            read_data = list(read_csv)

        with open(json_file, "w") as file_json:
            json.dump(read_data, file_json)

        return True
    except FileNotFoundError:
        return False
