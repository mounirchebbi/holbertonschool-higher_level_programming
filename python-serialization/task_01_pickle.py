#!/usr/bin/python3
# task_01_pickle.py
"""Module that defines CustomObject class"""
import pickle
import os


class CustomObject:
    """pickle self serialzer object"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return filename
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        if not os.path.exists(filename):
            return None
        try:
            with open(filename, 'rb') as file:
                new_object = pickle.load(file)

            return new_object
        except Exception as e:
            return None
