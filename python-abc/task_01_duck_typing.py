#!/usr/bin/python3
# task_01_duck_typing.py
"""Shapes module to apply duck typing on subclasses"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """abstract class Shape"""

    @abstractmethod
    def area(self):
        """abstract area method"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract perimeter method"""
        pass


class Rectangle(Shape):
    """Rectangle subclass of Shape"""
    def __init__(self, width, height):
        """Rectangle class constructor"""
        self.width = width
        self.height = height

    def area(self):
        """area method def"""
        return self.width * self.height

    def perimeter(self):
        """perimeter method def"""
        return (self.width + self.height) * 2


class Circle(Shape):
    """Circle subclass of shape"""
    def __init__(self, radius):
        """circle class constructor"""
        self.radius = abs(radius)

    def area(self):
        """area method def"""
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        """perimeter method def"""
        return self.radius * 2 * math.pi


def shape_info(shape):
    """stand alone function ducktyping area() perimeter()"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
