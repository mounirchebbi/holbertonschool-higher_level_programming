#!/usr/bin/python3
# 10-square.py
"""import Rectangle module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
