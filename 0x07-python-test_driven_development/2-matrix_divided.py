#!/usr/bin/python3
""" Module which contains a functions that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list:
        raise TypeError(error)
    for row in matrix:
        if type(row) != list:
            raise TypeError(error)
    if len(matrix) == 0:
        raise TypeError(error)
    for row in matrix:
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError(error)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    return [list(map(lambda fun: round(fun / div, 2), ele)) for ele in matrix]
