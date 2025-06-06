#!/usr/bin/python3
""" It contains the functions:
serialize_to_xml
deserialize_from_xml
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serializes the dictionary into XML
    and save it to the given filename """

    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)
        item.set("type", type(value).__name__)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """ Returns a deserialized Python dictionary """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for item in root:
        text = item.text
        type_str = item.attrib.get("type", "str")

        # Converting text by type
        if type_str == "int":
            value = int(text)
        elif type_str == "float":
            value = float(text)
        elif type_str == "bool":
            value = text.lower() == "true"
        else:
            value = text

        result[item.tag] = value

    return result
