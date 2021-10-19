#!/usr/bin/python3
"""function"""


from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.id = id
        super().__init__(self.id)

        if not isinstance(width, int):
            raise TypeError(f"{self.width} must be an integer")
        if width <= 0:
            raise ValueError(f"{self.width} must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError(f"{self.height} must be an integer")
        if height <= 0:
            raise ValueError(f"{self.height} must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError(f"{self.x} must be an integer")
        if x <= 0:
            raise ValueError(f"{self.x} must be > 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError(f"{self.y} must be an integer")
        if y <= 0:
            raise ValueError(f"{self.y} must be > 0")
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.width} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.width} must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y