#!/usr/bin/python3
"""displays the value of the variable"""


from sys import argv
import requests as r

if __name__ == "__main__":
    res = r.get(argv[1])
    print(res.headers["X-Request-Id"])
