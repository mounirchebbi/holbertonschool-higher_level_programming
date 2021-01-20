#!/usr/bin/python3
"""Definition of class Student"""


class Student:
    """A student"""

    def __init__(self, first_name, last_name, age):
        """New Student.

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of student"""
        return self.__dict__
