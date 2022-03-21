#!/usr/bin/python3
"""takes in a URL and an email address"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    dict = {'email': argv[2]}
    html = post(argv[1], data=dict)
    print(html.text)
