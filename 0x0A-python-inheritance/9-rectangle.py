#!/usr/bin/python3
"""function that print rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        return(self.__width * self.__height)

    def __str__(self):
        string = f"[{type(self).__name__}] {self.__width}/{self.__height}"
        return string
