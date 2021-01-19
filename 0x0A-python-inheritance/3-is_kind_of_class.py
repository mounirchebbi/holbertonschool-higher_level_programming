#!/usr/bin/python3
"""module defines function that returns True if object is a sub/class"""


def is_kind_of_class(obj, a_class):
    """ determines if a obj is an instance of a class that is inherited
    from a_class
    Args:
        obj (object): object to evaluate
        a_class(class): class to evaluate
    Returns:
        True returns True if object/inherited object is an instance of a_class
        False if otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
