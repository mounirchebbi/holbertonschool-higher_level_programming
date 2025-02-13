#!/usr/bin/python3
# 5-save_to_json_file.py
"""Module that defines save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """obj -> json file """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
