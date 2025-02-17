#!/usr/bin/python3
# task_00_basic_serialization.py
"""Module that performs basic serialization dump load"""
import json


def serialize_and_save_to_file(data, filename):
    """json dump data"""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """json load data"""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
