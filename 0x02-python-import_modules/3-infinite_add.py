#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    s = 0
    args = argv[1:]
    for i in args:
        s += int(i)
    print(s)
