#!/usr/bin/python3
"""
create rectangle class and the white and white
"""


class Rectangle():
    """
    init the rectangle class
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        return the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        errors to the width
        """
        if type(value) is not int:
            raise TypeError("widht must be an integer")
        elif value < 0:
            raise ValueError("widht must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        errors to the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value
