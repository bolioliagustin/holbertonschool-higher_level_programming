#!/usr/bin/python3
"""function that write string to file"""


def append_write(filename="", text=""):
    """write string to file and return the number of character"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
