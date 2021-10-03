#!/usr/bin/python3


def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div is not int:
        raise TypeError("div must be a number")
    #matrix must be a list of lists  of ints/floats
        #raise TypeError("matrix bust me a matrix (list of lists) of integers/floats")
    #each row of matrix must be the same size
        #raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
