#!/usr/bin/python3
# 100-append_after.py
"""Module that defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """search string in file append after new string"""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(new_lines)
