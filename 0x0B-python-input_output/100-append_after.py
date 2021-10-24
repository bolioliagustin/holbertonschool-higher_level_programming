#!/usr/bin/python3
""" function insert string in text file """


def append_after(filename="", search_string="", new_string=""):
    """insert string"""
    i = ""

    with open(filename) as a:

        for line in a:
            i += line

            if search_string in line:
                i += new_string

    with open(filename, "w") as f:
        f.write(i)
