#!/usr/bin/python3
"""print pascal triangle"""


def pascal_triangle(n):
    """return pascal triangle"""
    if n <= 0:
        return []

    i = []
    for fila in range(n):
        i.append([1])

        for a in range(1, fila):
            i[fila].append(i[fila - 1][a - 1] + i[fila - 1][a])

        if fila is not 0:
            i[fila].append(1)
    return i