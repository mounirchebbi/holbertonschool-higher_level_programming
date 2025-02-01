#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    counter = 0
    for item in my_list:
        try:
            if counter < x:
                print(item, end="")
                counter += 1
        except Exception as e:
            print("Error detected")
    print()
    return counter
