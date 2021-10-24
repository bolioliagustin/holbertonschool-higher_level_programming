#!/usr/bin/python3
"""function that writes object to file using JSON"""


import json


def load_from_json_file(filename):
    with open(filename, "r") as f:
        return json.load(f)
