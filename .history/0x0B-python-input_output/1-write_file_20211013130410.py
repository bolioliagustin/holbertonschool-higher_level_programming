#!/usr/bin/python3
"""function that write string to file"""


def write_file(filename="", text=""):
    """write string to file and return the number of character"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
