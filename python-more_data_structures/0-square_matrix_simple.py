#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append([x*x for x in row])
    # less readable:
    # new_matrix = [[x*x for x in row] for row in matrix]
    return new_matrix
