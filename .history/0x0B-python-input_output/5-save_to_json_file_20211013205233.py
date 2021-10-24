#!/usr/bin/python3
"""function that writes object to file using JSON"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        my_json = json.dumps(my_obj)
        return f.write(my_json)
