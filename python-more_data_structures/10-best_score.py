#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    max_key = None
    max_value = float('-inf')#lowest possible value

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
