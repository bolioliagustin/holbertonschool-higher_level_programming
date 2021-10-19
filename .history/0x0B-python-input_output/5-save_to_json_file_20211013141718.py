#!/usr/bin/python3
"""function that writes object to file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        my_json = json.load(my_obj)
        f.write(my_json)
