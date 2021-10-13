#!/usr/bin/python3
""""define class"""


class Square:
    """define init"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position