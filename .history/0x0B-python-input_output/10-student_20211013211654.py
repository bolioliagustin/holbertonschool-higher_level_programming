#!/usr/bin/python3
"""function  that create class student"""

class Student():
    """crate class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if type(attrs) is list:
            i = {}

            for x in attrs:
                if x in self.__dict__:
                    i[x] = self.__dict__[x]
            return i

        return self.__dict__