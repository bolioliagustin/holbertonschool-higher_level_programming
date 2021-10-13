#!/usr/bin/python3
"""funcion checks if obj inherited from a_class"""


def inherits_from(obj, a_class):
    """print True and False"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
