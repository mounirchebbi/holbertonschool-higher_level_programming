#!/usr/bin/python3
# 3-square.py
"""Define Class"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        self.size = size     # size public property size
    
    @property                  #decoration : getter for private attribute __size
    def size(self):
        return self.__size
    
    @size.setter               #decoration : sette for private attribute __size
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
