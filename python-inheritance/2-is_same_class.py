#!/usr/bin/python3
# 2-is_same_class.py
"""Verify if object is instance of specific class"""


def is_same_class(obj, a_class):
    """Returns true if obj is instance of a_class"""

    if type(obj, a_class):
        return True
    else:
        return False
