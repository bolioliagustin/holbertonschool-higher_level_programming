#!/usr/bin/python3
""" function that return JSON
representation of an object"""


import json


def from_json_string(my_obj):
    """return object"""
    return json.loads(my_obj)
