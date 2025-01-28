#!/usr/bin/python3
# 2-args.py
if __name__ == "__main__":
    """print arguments"""
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        i = 0
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(len(sys.argv)-1):
            print("{}: {}".format(i+1, sys.argv[i+1]))
