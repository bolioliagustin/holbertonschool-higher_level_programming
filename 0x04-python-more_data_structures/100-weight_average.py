#!/usr/bin/python3
def weight_average(my_list=[]):
    di = 0
    d = 0
    if not my_list:
        return 0
    for i in my_list:
        di += (i[0]*i[1])
        d += i[1]
    return di/d
