#!/usr/bin/python3
""" function insert string in text file """


def append_after(filename="", search_string="", new_string=""):
    """
    insert text
    """
    tx = ""

    with open(filename) as a:

        for line in a:
            tx += line

            if search_string in line:
                tx += new_string

    with open(filename, "w") as c:
        c.write(tx)