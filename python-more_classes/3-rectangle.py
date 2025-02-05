#!/usr/bin/python3
# 3-rectangle.py
"""Defines Rectangle Class"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        row = ""
        if self.__height == 0 or self.__width == 0:
            return row
        else:
            if self.__height > 1:
                for i in range(self.__height-1):
                    row += "#" * self.__width + "\n"
            row += "#" * self.__width
            return row
