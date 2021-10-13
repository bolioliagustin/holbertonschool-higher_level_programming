#!/usr/bin/python3
"""function that print rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


def Rectangle(BaseGeometry):
    """fuction Rectangle returns errors inherits BaseGeometry"""
    def __init__(self, width, height):
        self.__width=  width
        self.__height=  height
        self.integer_validator("width", width)
        self.integer_validator("height", height)