#!/usr/bin/python3
# 2-is_same_class.py
"""Module that verifies if object is instance of specific class"""


def is_same_class(obj, a_class):
    """function that returns true if obj is instance of a_class"""
    return type(obj) is a_class
