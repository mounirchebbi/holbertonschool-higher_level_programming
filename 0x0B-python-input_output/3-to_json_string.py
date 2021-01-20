#!/usr/bin/python3
"""function from string-to-JSON """
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string"""
    return json.dumps(my_obj)
