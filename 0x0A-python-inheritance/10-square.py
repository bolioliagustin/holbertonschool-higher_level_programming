#!/usr/bin/python3
"""function that print rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """clas Square"""
    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
        super().__init__(size, size)