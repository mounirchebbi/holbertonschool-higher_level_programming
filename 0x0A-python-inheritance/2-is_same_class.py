#!/usr/bin/python3
"""Definition of class checker"""


def is_same_class(obj, a_class):
    """Determines if object is exact instance of a class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        if object is exact instance of a class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
