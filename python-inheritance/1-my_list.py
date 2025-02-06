#!/usr/bin/python3
# 1-my_list.py
"""List module"""


class MyList (list):
    """List clas that inherits from list"""

    def print_sorted(self):
        """method that print a sorted list"""
        print(sorted(self))
