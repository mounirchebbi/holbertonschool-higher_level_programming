#!/usr/bin/python3
# 8-class_to_json.py
"""Modules that defines class_to _json"""


def class_to_json(obj):
    """convert class to serializable dict"""

    serializable_obj = {}
    for key, value in obj.__dict__.items():
        # case if value is serializable
        if isinstance(value, (int, str, float, bool, list, dict)):
            serializable_obj[key] = value
        # case of tuple or set convert to list
        elif isinstance(value, (tuple, set)):
            serializable_obj[key] = list(value)
        # default convert to string
        else:
            serializable_obj[key] = str(value)
    return serializable_obj
