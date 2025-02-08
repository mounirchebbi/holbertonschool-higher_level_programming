#!/usr/bin/python3
# 100-my_int.py
"""New int module"""


class MyInt(int):
    "redifine init for == and != operations"
    # use help(int) to find the right methods

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
