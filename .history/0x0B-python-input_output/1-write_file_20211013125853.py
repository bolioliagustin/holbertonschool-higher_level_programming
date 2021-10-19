#!/usr/bin/python3
"""function that write string to file"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
