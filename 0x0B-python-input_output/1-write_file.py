#!/usr/bin/python3
"""module definitions of a file writing function"""


def write_file(filename="", text=""):
    """Write string to file

    Args:
        filename (str): file name
        text (str): text to write
    Returns:
        number of characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
