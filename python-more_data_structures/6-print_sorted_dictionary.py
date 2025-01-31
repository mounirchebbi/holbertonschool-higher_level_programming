#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    sorted_keys = list(a_dictionary.keys())
    sorted_keys.sort()
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
