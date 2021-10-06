#!/usr/bin/python3
"""
Print division elements of the matrix
"""


def matrix_divided(matrix, div):
    """
    Funcion to divided elements of the matrix
    """
    error = "matrix must be a matrix (list of list) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)
    if (len(matrix[0])) != (len(matrix[1])):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    list1 = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(error)
        list2 = []
        for x in i:
            if not isinstance(x, (int, float)):
                raise TypeError(error)
            list2.append(round(x/div, 2))
        list1.append(list2)
    return list1
