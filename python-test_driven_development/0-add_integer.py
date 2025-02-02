#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """
    Adds two ints.

    Parameters:
    a (int or float): first int
    b (int or float ): second int, default = 98

    Returns:
    int : sum a + b

    Raises:
    TypeError if a or b not int or float

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

print(add_integer(1,'b'))
