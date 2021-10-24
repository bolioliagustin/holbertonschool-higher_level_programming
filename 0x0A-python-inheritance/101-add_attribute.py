#!/usr/bin/python3
"""function that add_attribute"""


def add_attribute(obj, name, value):
    """create class  """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
