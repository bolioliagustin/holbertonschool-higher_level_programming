#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            k += 1
        except:
            pass
    print()
    return (k)
