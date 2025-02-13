#!/usr/bin/python3
# 6-load_from_json_file.py
"""Module that defines save_to_json_file"""
import json


def load_from_json_file(filename):
    """json file -> obj"""
    with open(filename, 'r') as file:
        obj = json.load(file)
    return json.load()
