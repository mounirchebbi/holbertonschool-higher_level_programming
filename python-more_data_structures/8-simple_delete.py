#!/usr/bin/python3
# 8-simple_delete.py

def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, 0)
    return a_dictionary
