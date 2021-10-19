#!/usr/bin/python3
"""function returns the dictionary
description with simple data structure"""


def class_to_json(obj):
    """return dictionary"""
    return obj.__dict__
