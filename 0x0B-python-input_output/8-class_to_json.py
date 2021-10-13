#!/usr/bin/python3
'''module that contains class_to_json function'''


def class_to_json(obj):
    '''returns a dictionary description with simple structure data'''
    return obj.__dict__('__dict__')
