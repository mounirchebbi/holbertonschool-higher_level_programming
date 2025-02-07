#!/usr/bin/python3
# 4-inherits_from.py
"""Module checks if object inherits from specefic class"""


def inherits_from(obj, a_class):
    """Returns True if obj inherits from a_class"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
