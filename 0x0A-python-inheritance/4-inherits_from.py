#!/usr/bin/python3
"""module defines inherits_from function determines if object is a subclass"""


def inherits_from(obj, a_class):
    """determines if a obj is a subclass of a_class
    from a_class
    Args:
        obj (object): object to evaluate
        a_class(class): class to evaluate
    Returns:
        True returns True if obj is an inherited object of a_class
        False if otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
