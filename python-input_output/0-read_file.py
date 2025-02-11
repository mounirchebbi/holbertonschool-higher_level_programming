#!/usr/bin/python3
# 0-read_file.py
"""Module that defines function read_file"""


def read_file(filename=""):
    """function that reads a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
