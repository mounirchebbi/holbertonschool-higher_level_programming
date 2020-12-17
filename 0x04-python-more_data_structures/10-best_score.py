#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    list = a_dictionary.items()
    list = sorted(list, key=lambda tup: tup[1], reverse=True)
    a, b = list[0]
    print(a)
    return a
