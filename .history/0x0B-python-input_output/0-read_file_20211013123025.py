#!/usr/bin/python3
"""function that read file"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print (line, end="")