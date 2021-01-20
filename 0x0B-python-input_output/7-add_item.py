#!/usr/bin/python3
"""Load, add, save from json_file"""
import json

from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except:
    with open(filename, "a") as f:
        items = []

for arg in argv[1:]:
    items.append(arg)
save_to_json_file(items, filename)
