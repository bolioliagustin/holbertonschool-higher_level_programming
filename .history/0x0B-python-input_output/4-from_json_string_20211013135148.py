#!/usr/bin/python3
""" function that return an object 
represented by a JSON string"""
import json


def from_json_string(my_obj):
    return json.loads(my_obj)
