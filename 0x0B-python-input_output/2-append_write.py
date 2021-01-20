#!/usr/bin/python3
"""function that appends to file"""


def append_write(filename="", text=""):
    """Append string to the end of file

    Args:
        filename (str): The name of the file
        text (str): string to append
    Returns:
        number of characters
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
