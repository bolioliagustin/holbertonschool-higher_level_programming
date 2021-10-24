#!/usr/bin/python3
"""function that read file"""


def read_file(filename=""):
    """read file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
