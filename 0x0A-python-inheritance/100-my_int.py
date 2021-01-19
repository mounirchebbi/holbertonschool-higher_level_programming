#!/usr/bin/python3
"""module defines class MyInt"""


class MyInt(int):
    """Invert operators"""

    def __eq__(self, value):
        """Override == opeartor with !="""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with =="""
        return self.real == value
