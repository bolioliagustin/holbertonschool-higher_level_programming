#!/usr/bin/python3
"""function"""


from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.id = id
        super().__init__(self.id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        """errors to the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """errors to the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """errors to the x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """errors to the y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """define area"""
        return(self.__width * self.__height)

    def display(self):
        """print rectangle"""
        if self.__width == 0 or self.__height == 0:
            print()
        for l in range(self.__y):
            print()
        for s in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for x in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        string = f"[{type(self).__name__}]({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return string

    def update(self, *args, **kwargs):
        """ that argument asignad """
        if len(args) > 0:
            for a in range(len(args)):
                if a == 0:
                    self.id = args[a]
                if a == 1:
                    self.__width = args[a]
                if a == 2:
                    self.__height = args[a]
                if a == 3:
                    self.__x = args[a]
                if a == 4:
                    self.__y = args[a]
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
        """ returns  dictionary of a Rectangle """
        return {
            'id': self.id, 'width': self.width,
            'height': self.height, 'x': self.x, 'y': self.y
        }