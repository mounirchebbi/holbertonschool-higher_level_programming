#!/usr/bin/python3
# 12-pascal_triangle.py
"""Module that defines pascal_triangle function"""


def pascal_triangle(n):
    """create pascal triangle of size n"""
    triangle = []

    if n > 0:
        for row in range(n):
            triangle_row = [1] * (row + 1)

            for i in range(1, row):
                triangle_row[i] = triangle[row - 1][i - 1]\
                                  + triangle[row - 1][i]

            triangle.append(triangle_row)

    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
