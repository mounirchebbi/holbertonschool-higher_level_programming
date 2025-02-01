#!/usr/bin/python3
# d100-weight_average.py

def weight_average(my_list=[]):
    if (my_list is None) or (len(my_list) == 0):
        return 0
    
    _sum = 0
    count = 0

    for _tuple in my_list:
        _sum += _tuple[0] * _tuple[1]
        count += _tuple[1]

    return (_sum/count)
