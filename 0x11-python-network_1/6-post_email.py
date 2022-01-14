#!/usr/bin/python3
"""takes in a URL and an email address"""


from sys import argv
import requests as r

if __name__ == "__main__":
    email = argv[2]
    data = {'email': email}
    res = r.post(argv[1], data=data.encode('utf-8'))
    print(res.request.body)
