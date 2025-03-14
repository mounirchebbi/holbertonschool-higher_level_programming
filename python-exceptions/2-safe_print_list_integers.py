#!/usr/bin/python3
#

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    printed_counter = 0
    for item in my_list:
        try:
            if counter < x:
                try:
                    if isinstance(item, int):
                        print("{:d}".format(item), end="")
                        printed_counter += 1
                    counter += 1
                except Exception as e:
                    print("input type error")
        except IndexError as e:
            print("list index out of range")
    print()
    return printed_counter
