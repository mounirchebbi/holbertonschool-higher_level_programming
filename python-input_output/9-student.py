#!/usr/bin/python3
# 9-student.py
"""Modules that defines class_to _json"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """self dict to json dict serialize"""
        json_list = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int, float, bool, list, dict)):
                json_list[key] = value
            elif isinstance(value, (tuple, set)):
                json_list[key] = list(value)
            else:
                json_list[key] = str(value)
        return json_list
