#!/usr/bin/python3
"""
function that adds
"""


def add_integer(a, b=98):
    """
    function that returns
    the sum of two int or float
    a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)

    return a + b
