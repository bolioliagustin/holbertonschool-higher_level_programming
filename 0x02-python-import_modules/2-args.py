#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv[1:]
    i = 1
    num = len(args)
    if num == 0:
        print("{} arguments.".format(num))
    elif num == 1:
        print("{} argument:".format(num))
    else:
        print("{} arguments:".format(num))
    while i <= num:
        print("{}:".format(i), argv[i], end="")
        print("")
        i += 1
