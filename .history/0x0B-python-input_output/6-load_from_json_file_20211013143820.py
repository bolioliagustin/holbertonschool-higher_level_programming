#!/usr/bin/python3
"""function that writes object to file using JSON"""
import json


def load_to_json_file(filename):
    with open(filename, "w", encoding="utf-8") as f:
        return json.loads(f)
