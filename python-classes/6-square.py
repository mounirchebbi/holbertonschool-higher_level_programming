#!/usr/bin/python3
# 5-square.py
"""Square"""


class Square:
    """define a square"""

    def __init__(self, size=0, pos_tuple=(0, 0)):
        self.size = size
        self.position = pos_tuple

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size > 0:
            for y in range(self.__position[0]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[1] + "#" * self.__size)
        else:
            print()
