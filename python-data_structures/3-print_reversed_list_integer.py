#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)-1, -1, -1):
        print("{:d}".format(my_list[i]))
