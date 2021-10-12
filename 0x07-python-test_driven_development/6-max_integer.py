#!/usr/bin/python3
""""max integer in a list"""


def max_integer(list=[]):
    """ return the max integer in a list of integers
         list is emptythe function returns None
    """
    if len(list) == 0:
        return None
    r = list[0]
    l = 1
    while l < len(list):
        if list[l] > r:
            r = list[l]
        l += 1
    return r