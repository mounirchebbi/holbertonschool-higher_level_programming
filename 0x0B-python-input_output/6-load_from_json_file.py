#!/usr/bin/python3
"""function that reads from JSON"""
import json


def load_from_json_file(filename):
    """Create Python object from a JSON"""
    with open(filename) as f:
        return json.load(f)
