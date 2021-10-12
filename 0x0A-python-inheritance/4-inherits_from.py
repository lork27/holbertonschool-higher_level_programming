#!/usr/bin/python3
'''function that checks if object is an instance of a class
that inherited, directly or not, from another class
'''


def inherits_from(obj, a_class):
    '''
    param: obj to check if it matches with a_class param
    param: a_class will used for comparison with obj
    '''
    if type(obj) == a_class:
        return False
    else:
        return True
