#!/usr/bin/python3
# 2-print_alphabet.py

"""one loop, print alphabet"""
for i in range(ord('a'), ord('z')+1):
    print("{}".format(chr(i)), end="")
