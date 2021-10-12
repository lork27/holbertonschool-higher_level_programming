#!/usr/bin/python3
'''module that contains same class function'''


def is_same_class(obj, a_class):
    '''returns true if object is the exact same as class'''
    if type(obj) == a_class:
        return True
    else:
        return False
