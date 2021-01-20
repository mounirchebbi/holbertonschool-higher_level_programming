#!/usr/bin/python3
"""modules that defines read file function"""


def read_file(filename=""):
    """Print the content of file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
