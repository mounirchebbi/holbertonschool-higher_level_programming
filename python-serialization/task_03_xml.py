#!/usr/bin/python3
# task_03_xml.py
"""Module to serialize and deserialize xml dict"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary to XML file"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, "wb") as xml_file:
        tree.write(xml_file)


def deserialize_from_xml(filename):
    """Deserialize XML file into a dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}
    for item in root:
        result_dict[item.tag] = item.text

    return result_dict
