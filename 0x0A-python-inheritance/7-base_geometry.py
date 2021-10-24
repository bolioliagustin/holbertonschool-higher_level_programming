#!/usr/bin/python3
"""funcion that print errors class"""


class BaseGeometry():
    """print class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """print errors"""
        self.name = name
        self.value = value
        if type (value) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be grater than 0")
        return value
