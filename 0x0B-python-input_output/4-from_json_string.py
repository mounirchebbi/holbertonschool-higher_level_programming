#!/usr/bin/python3
"""function from JSON to object """
import json


def from_json_string(my_str):
    """Return Python representation of a JSON string"""
    return json.loads(my_str)
