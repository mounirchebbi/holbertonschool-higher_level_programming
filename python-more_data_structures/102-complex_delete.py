#!/usr/bin/python3
# 102-complex_delete.py

def complex_delete(a_dictionary, value):
    if a_dictionary is None or value is None:
        return None
    for k, v in a_dictionary.items():
        if v is value:
            a_dictionary.pop(k)

    return (a_dictionary)
