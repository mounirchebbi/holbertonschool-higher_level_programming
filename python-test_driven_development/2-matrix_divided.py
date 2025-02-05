#!/usr/bin/python3
# 2-matrix_divided.py
""" Matrix elements divider"""


def matrix_divided(matrix, div):
    """Divides elements of matrix by div"""
    # check matrix
    if not isinstance(matrix, list) or\
        not all(isinstance(row, list) for row in matrix) or\
        not all(isinstance(val, (int, float)) for row in matrix
                for val in row):
        raise TypeError("matrix must be a matrix\
                         (list of lists) of integers/floats")

    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    else:
        new_matrix = []
        for row in matrix:
            new_row = []
            for val in row:
                new_row.append(round(val / div, 2))
            new_matrix.append(new_row)
    # better version
    # new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix
