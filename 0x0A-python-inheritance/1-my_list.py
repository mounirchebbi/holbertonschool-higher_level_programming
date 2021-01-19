#!/usr/bin/python3
"""Definition of MyList"""


class MyList(list):
    """Implements list class."""

    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
