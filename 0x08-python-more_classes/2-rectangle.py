  #!/usr/bin/python3
"""
create rectangle class and the white and white
"""


class Rectangle():
    """init the rectangle class"""
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

    @property
    def width(self):
        """return the width"""
        return self.__width

    @property
    def height(self):
        """return height"""
        return self.__height

    @width.setter
    def width(self, value):
        """errors to the width"""
        if not isinstance(value, int):
            raise TypeError("widht must be an integer")
        elif value < 0:
            raise ValueError("widht must be >=0")
        self.__width = value

    @height.setter
    def height(self, value):
        """errors to the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value  
    
    def area(self):
        """return area"""
        return(self.width * self.height)

    def perimeter(self):
        """return perimeter"""
        if self.__width == 0 and self.__height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
