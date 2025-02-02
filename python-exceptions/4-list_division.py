#!/usr/bin/python3
# 4-list_division.py

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    counter = 0

    while counter < list_length:
        result = 0
        try:
            result = my_list_1[counter] / my_list_2[counter]
        except Exception as e:
            if counter >= len(my_list_1) or counter >= len(my_list_2):
                print("out of range")
            elif (not isinstance(my_list_1[counter], int) or
                  not isinstance(my_list_2[counter], int)):
                print("wrong type")
            elif my_list_1[counter] == 0 or my_list_2[counter] == 0:
                print("division by 0")
        finally:
            new_list.append(result)
        counter += 1

    return new_list
