#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for idx in range(len(matrix[row])):
            print("{:d}".format(matrix[row][idx]), end="")
            if (idx != len(matrix[row]) - 1):
                print(" ", end="")
        print("")
