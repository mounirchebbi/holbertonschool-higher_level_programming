#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    a = 0
    b = 0
    for item in my_list:
        a += (item[0] * item[1])
        b += item[1]
    return (a / b)
