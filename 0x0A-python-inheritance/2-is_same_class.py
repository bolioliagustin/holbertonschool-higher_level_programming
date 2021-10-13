#!/usr/bin/python3
"""funcion that return True if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Print True or False"""
    return type(obj) is a_class
