#!/usr/bin/python3
"""create class rectangle and values"""


class Rectangle():
    """create class rectangle """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def area(self):
        """return area"""
        return(self.width * self.height)

    def perimeter(self):
        """return perimeter"""
        return ((self.width * 2) + (self.height * 2))

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """error for the value of the width"""
        if type(value) is not int:
            raise TypeError("widht must be an integer")
        elif value < 0:
            raise ValueError("widht must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """errors to the values of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def __str__(self):
        """print the rectangle"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))
        return string
