#!/usr/bin/python3
"""create class rectangle and values"""


class Rectangle():
    """create class rectangle """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height


    def area(self):
        """return area"""
        return(self.width * self.height)

    def perimeter(self):
        """return perimeter"""
        if self.__width == 0 and self.__height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    @property
    def width(self):
        """return width"""
        return self.__width

    @property
    def height(self):
        """return height"""
        return self.__height

    @width.setter
    def width(self, value):
        """error for the value of the width"""
        if not isinstance(value, int):
            raise TypeError("widht must be an integer")
        elif value < 0:
            raise ValueError("widht must be >=0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """errors to the values of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value
