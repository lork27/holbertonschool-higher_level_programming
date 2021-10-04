#!/usr/bin/python3
""" Module that contains functions that prints square of # of Nth size """


def print_square(size):
    """print_square: function that prints square of #
    parameters:
        size:number of # that should be printed
    Raised:
        TyperError: if size is less than 0 or not int
    """
    if size is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
