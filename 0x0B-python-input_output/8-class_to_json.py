#!/usr/bin/python3
'''module that contains class_to_json function'''
import json


def class_to_json(obj):
    '''returns a dictionary description with simple structure data'''
    return vars(obj)
