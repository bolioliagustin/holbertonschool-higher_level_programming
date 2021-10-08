#!/usr/bin/python3
"""
divide text  
"""


def text_indentation(text):
    """
   divide text to the simbol in one string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = ""
    chars = ['.', '?', ':']
    for c in text:
        i += c
        if c in chars:
            print(i.lstrip())
            print()
            i = ""
    if not any(c in i for c in chars):
        print(i.lstrip(), end="")

