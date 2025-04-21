#!/usr/bin/python3
"""Module text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    '.', '?' and ':'.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    i = 0
    while i < len(text):
        if text[i] in special_chars:
            print(text[i], end="\n\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
