#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum = 0
    for num in my_set:
        sum += num
    return sum
