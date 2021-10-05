#!/bin/usr/python3
""" Module which contains a function that adds two integers """


def add_integer(a, b=98):
    """add_integer: functions that adds two numbers
    parameters:
        a: first integer
        b: second integer, its 98 if nothing is passed
    Raised:
        TypeError: if a or b not int/float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")


    return int(a) + int(b)
