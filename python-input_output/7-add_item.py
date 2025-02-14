#!/usr/bin/python3
# 7-add_item.py
"""Module that save argument into json file then loads and print them"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv
json_list = []
for i in range(1, len(args)):
    json_list.append(args[i])
save_to_json_file(json_list, "add_item.json")
print(load_from_json_file("add_item.json"))
