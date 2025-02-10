#!/usr/bin/python3
# task_01_duck_typing.py
"""Shapes module to apply duck typing on subclasses"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """abstract class Shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    """subclass Rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Circle(Shape):
    """subclass Circle"""
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.141592653589793

    def area(self):
        return (self.radius ** 2) * self.pi

    def perimeter(self):
        return self.radius * 2 * self.pi


# stand alone function
def shape_info(shape):
    print(f"Area: {shape.area()}\nPerimeter:{shape.perimeter()}")
