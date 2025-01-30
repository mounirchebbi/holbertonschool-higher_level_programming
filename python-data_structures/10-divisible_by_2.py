#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    if (len(my_list) <= 0):
        return None
    new_list = []
    for num in my_list:
        if num % 2:
            new_list.append(False)
        else:
            new_list.append(True)
    return new_list
