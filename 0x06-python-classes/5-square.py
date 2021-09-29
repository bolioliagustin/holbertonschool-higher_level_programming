#!/usr/bin/python3
""""defino class"""


class Square:
    """define init"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """defino area"""
        return (self.size ** 2)

    @property
    def size(self):
        """devuelvo size"""
        return self.__size

    @size.setter
    def size(self, value):
        """errors"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for l in range(self.__size):
                    print("#", end="")
                print()
