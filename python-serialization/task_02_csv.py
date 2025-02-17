#!/usr/bin/python3
# task_02_csv.py
"""Module to convert csv to json"""
import csv
import json


def convert_csv_to_json(csv_file):
    """return true when convertion successful"""
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            try:
                with open("data.json", 'w') as file2:
                    json.dump(list(reader), file2)
                return True
            except Exception as e1:
                return False
    except Exception as e:
        return False
