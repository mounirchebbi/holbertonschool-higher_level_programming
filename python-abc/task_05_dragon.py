#!/usr/bin/python3
# task_05_dragon.py
"""Module to test mixin"""


class SwimMixin:
    """Defines mixin class SwimMixin"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Defines mixin class FlyMixin"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """class inherits from SwimMixin and FlyMixin"""
    def roar(self):
        print("The dragon roars!")
