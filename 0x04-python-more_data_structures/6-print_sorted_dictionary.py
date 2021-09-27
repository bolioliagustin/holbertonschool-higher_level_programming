#!/usr/bin/python3
def print_sorted_dictionary(a_directonaty):
    for i in sorted(a_directonaty):
        x = a_directonaty.get(i)
        print ("{}".format(i), end=": ")
        print (x)
