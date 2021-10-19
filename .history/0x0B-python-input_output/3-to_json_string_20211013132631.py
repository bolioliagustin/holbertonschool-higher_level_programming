#!/usr/bin/python3
""" function that return JSON 
representation of an object"""
import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
