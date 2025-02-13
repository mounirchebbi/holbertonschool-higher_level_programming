#!/usr/bin/python3
# 2-append_write.py
"""Module that defines append_write function"""


def append_write(filename="", text=""):
    """append tyext to file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
