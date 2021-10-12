#!/usr/bin/python3
'''
module that contains inherits_from function
'''


def inherits_from(obj, a_class):
    '''
    Returns true if object is an instance of class
    '''
    if type(obj) == a_class or isinstance(obj, a_class) is not False:
        return False
    else:
        return True
