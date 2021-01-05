#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Initialization

        Args:
            size (int): Square Size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Return square area"""
            return (self.__size * self.__size)
