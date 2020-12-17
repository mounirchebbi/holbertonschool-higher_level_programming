#!/usr/bin/python3
def uniq_add(my_list=[]):
    history = []
    sum = 0
    for i in range(len(my_list)):
        if i == 0:
            history.append(my_list[i])
            sum += my_list[i]
        if history.count(my_list[i]) == 0:
            sum += my_list[i]
            history.append(my_list[i])
    return sum
