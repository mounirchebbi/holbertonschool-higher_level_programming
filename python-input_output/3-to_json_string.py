#!/usr/bin/python3
# 3-to_json_string.py
"""Module that defines to_json_string"""
import json


def to_json_string(my_obj):
    """convert object to json string"""
    return json.dumps(my_obj)
