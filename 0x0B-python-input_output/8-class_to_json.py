#!/usr/bin/python3
"""definition of class-to-JSON function"""


def class_to_json(obj):
    """Return simple data structure"""
    return obj.__dict__
