#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
