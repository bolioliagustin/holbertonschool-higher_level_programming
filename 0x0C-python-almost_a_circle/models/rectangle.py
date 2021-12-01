#!/usr/bin/python3
"""function"""


from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return area"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """return string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height)

    def update(self, *args, **kwargs):
        """update"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """return dictionary"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
