#!/usr/bin/python3
# task_03_countediterator.py
"""Module for iterator class with counter"""


class CountedIterator:
    """define new iterator class"""
    def __init__(self, object):
        self.iterator = iter(object)
        self.counter = 0

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        return self.counter
