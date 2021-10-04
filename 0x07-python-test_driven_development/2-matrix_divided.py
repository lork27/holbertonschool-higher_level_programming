#!/usr/bin/python3
""" Module which contains a functions that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix_divided: functions that divides all elements of a matrix
    parameters:
        matrix: list of lists that contains numbers
        div: division factor of each elements of matrix
    Raised:
        TypeError: if each row is not the same as the others
        TypeError: if any row is not composed solely of ints or floats
        TypeError: if div is not a number
        ZeroDivisionError: if div is equal 0
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div is not int:
        raise TypeError("div must be a number")
    #matrix must be a list of lists  of ints/floats
        #raise TypeError("matrix bust me a matrix (list of lists) of integers/floats")
    #each row of matrix must be the same size
        #raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
