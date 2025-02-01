#!/usr/bin/python3
#

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for item in my_list:
        try:
            if counter < x:
                try:
                    if isinstance(item, int):
                        print("{:d}".format(item), end="")
                        counter += 1
                except Exception as e:
                    print("input type error")
        except Exception as e:
            print("list index error")
    print()
    return counter
