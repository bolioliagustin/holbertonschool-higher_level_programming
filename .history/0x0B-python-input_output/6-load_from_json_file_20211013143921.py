#!/usr/bin/python3
"""function that writes object to file using JSON"""
import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f)
