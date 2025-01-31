#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    # search and replace
    for idx in range(len(new_list)):
        if new_list[idx] == search:
            new_list[idx] = replace
    return new_list
