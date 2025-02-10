#!/usr/bin/python3
# task_02_verboselist.py
"""Module that extands list class"""


class VerboseList(list):
    """VerboseList class that extends list class"""
    def append(self, object):
        list = super().append(object)
        print(f"Added [{object}] to the list.")
        return list

    def extend(self, iterable):
        list = super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")
        return list

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        return super().remove(value)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list")
        return item
