#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    set_1 = []
    for i, k in a_dictionary.items():
        if k == value:
            set_1.append(i)
    for l in set_1:
        del a_dictionary[l]
    return a_dictionary
