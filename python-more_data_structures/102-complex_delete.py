#!/usr/bin/python3
# 102-complex_delete.py

def complex_delete(a_dictionary, value):
    if a_dictionary is None or value is None:
        return None
    _list = []
    for k, v in a_dictionary.items():
        if v is not value:
            _list.append((k, v))
    return (dict(_list))
