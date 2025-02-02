#!/usr/bin/python3
# 100-safe_print_integer_err.py

def safe_print_integer_err(value):
    import sys
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except TypeError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
