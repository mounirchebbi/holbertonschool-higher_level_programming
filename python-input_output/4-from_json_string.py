#!/usr/bin/python3
# 4-from_json_string.py
"""Module that defines from_json_string"""
import json

def from_json_string(my_str):
    """json string -> python object"""
    return json.loads(my_str)
