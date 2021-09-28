#!/usr/bin/python3
"""print size and errors"""


class Square:
    """print size and errors"""
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
