#!/bin/usr/python3


def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
    except:
        c = None
    finally:
        print("Inside result: {}".format(c))
        return c
