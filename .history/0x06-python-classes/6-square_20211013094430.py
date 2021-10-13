#!/usr/bin/python3
""""defino class"""


class Square:
    """define init"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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
            return
        for i in range(self.__position[1]):
            print()
        for x in range(self.__size):
            print("".join([" " for g in range(self.__position[0])]), end="")
            print("".join(["#" for o in range(self.__size)]))

    @property
    def position(self):
        """define position"""
        return self.__position

    @position.setter
    def position(self, value):
        """positions errors"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value