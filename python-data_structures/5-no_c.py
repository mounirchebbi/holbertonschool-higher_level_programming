#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    str_copy = ''
    for c in my_string:
        if c == 'c' or c == 'C':
            pass
        else:
            str_copy += c
    return str_copy
