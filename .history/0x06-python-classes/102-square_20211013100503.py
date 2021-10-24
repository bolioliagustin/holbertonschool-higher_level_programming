#!/usr/bin/python3
""" define class """


class Square:
    """ create Square """
    def __init__(self, size=0):
        self.size = size

    """ return size """
    @property
    def size(self):
        return self.__size

    """size attribute """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """area of square"""
    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.size == other.size

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.size > other.size

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.size != other.size

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.size < other.size

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.size >= other.size

    def __le__(self, other):
        if isinstance(other, Square):
            return self.size <= other.size
