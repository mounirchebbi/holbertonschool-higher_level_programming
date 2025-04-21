def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number and returns a new matrix rounded to 2 decimal places."""

    # Validate matrix is a list of lists with int or float elements
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate all rows are of the same size
    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    return [[round(num / div, 2) for num in row] for row in matrix]
