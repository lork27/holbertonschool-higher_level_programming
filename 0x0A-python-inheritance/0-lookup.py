#!/usr/bin/python3
'''Return list of avaiable attributes and methods of an object'''


def lookup(obj):
    '''Returns list of a dir of a given object as a parameter
    '''
    return list(dir(obj))
