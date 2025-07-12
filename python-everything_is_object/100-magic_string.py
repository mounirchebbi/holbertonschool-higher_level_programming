#!/usr/bin/python3
def magic_string(_count=[0]):
    _count[0] += 1
    return ", ".join(["BestSchool"] * _count[0])
"""_count is a mutable default argument (a list with one element).

It keeps track of how many times the function has been called.

Each call increases the count and returns "BestSchool" repeated that many times, joined with ", "."""
