#!/usr/bin/python3
# 1-write_file.py
"""Module that defines write_file function"""


def write_file(filename="", text=""):
    """write text to file and return number of characters written"""
    with open(filename, 'w', encoding='utf-8') as file:
        count = 0
        for c in text:
            file.write(c)
            count += 1

    return count
