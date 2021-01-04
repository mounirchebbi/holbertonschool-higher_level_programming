#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        out = fct(*args)
        return (out)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
