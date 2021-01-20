#!/usr/bin/python3
"""module defines add_attributes function"""


def add_attribute(obj, att, value):
    """Add attribute to object

    Args:
        obj (any): object
        att (str): attribute
        value (any): attribute value
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
