#!/usr/bin/python3
# 102-complex_delete.py

def complex_delete(a_dictionary, value):
    if a_dictionary is None or value is None:
        return None
    _keys = []
    for k, v in a_dictionary.items():
        if v is value:
            _keys.append(k)
# much better verion using filter
#   _keys = list(filter(lambda k: a_dictionnay[k] == value, a_dictionnary))
    if len(_keys) == 0:
        return (a_dictionary)
    for k in _keys:
        a_dictionary.pop(k)

    return (a_dictionary)
