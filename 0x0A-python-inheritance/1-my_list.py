#!/usr/bin/python3
"""Definition of an inherited list class MyList"""


class MyList(list):
    """Implements sorted printing"""

    def print_sorted(self):
        """Print list"""
        print(sorted(self))
