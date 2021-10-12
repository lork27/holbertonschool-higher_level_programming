#!/usr/bin
''' module that contains a function that checks if an object is
exactly an instance of the specified class'''


def is_same_class(obj, a_class):
    '''comment'''
    if type(obj) == a_class:
        return True
    else:
        return False
