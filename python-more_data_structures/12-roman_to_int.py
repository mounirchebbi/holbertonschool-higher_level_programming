#!/usr/bin/python3
# 12-roman_to_int.py

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or (roman_string is None):
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previous = 0
    for c in reversed(roman_string):
        if c not in roman_dict.keys():
            return 0
        value = roman_dict[c]
        if value >= previous:
            result += value
        else:
            result -= value
        previous = value
        value = 0
    return result
