#!/usr/bin/python3
"""Matrix elements divider"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div

    Args:
        matrix: list of lists of integers/floats
        div: number to divide matrix elements by

    Returns:
        A new matrix with elements divided by div and rounded
    Raises:
        TypeError: if matrix is not a list of lists of ints/floats,
                   or if rows are not of equal length,
                   or if div is not a number
        ZeroDivisionError: if div is zero
    """
    # Validate matrix structure and contents
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(val, (int, float))
                for row in matrix for val in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Validate uniform row size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Compute and return new matrix
    return [[round(val / div, 2) for val in row] for row in matrix]
