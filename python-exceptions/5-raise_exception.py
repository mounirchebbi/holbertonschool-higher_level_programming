#!/usr/bin/python3
# 5-raise_exception.py

def raise_exception():
    raise TypeError()

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
