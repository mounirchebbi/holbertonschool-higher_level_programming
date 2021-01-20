#!/usr/bin/python3
"""module that defines file number of lines counter"""


def number_of_lines(filename=""):
    """Return number of lines"""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
