#!/usr/bin/python3
# task_00_abc.py
"""Abstract class module"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """abstract class Animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """subclass Dog"""
    def __init__(self):
        pass

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclass Cat"""
    def __init__(self):
        pass

    def sound(self):
        return "Meow"
