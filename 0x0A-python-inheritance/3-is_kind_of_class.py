#!/usr/bin/python3
'''function that compares obj with class'''


def is_kind_of_class(obj, a_class):
    '''Function that return true if
    param: obj
    param: a_class
    Return true if they match False if not
    '''
    return isinstance(obj, a_class)
