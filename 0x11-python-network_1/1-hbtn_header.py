#!/usr/bin/python3
""" sends a request to the URL """


import urllib.request as r
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with r.urlopen(url) as res:
        print(res.getheader('X-Request-Id'))
