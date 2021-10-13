#!/usr/bin/python3
"""function that print rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.height = self.integer_validator("height", height)