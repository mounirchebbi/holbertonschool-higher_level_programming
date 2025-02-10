#!/usr/bin/python3
# task_04_flyingfish.py
"""Module to test multiple inheritance"""


class Fish:
    """defines fish class"""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """defines bird class"""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """defines flyingfish class that inherits from fish and bird"""
    def swim(self):
        print("The flying fish is soaring!")

    def fly(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
