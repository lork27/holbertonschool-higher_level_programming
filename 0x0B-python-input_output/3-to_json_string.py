#!/usr/bin/python3
'''module contains to_json_string function'''
import json


def to_json_string(my_str):
    '''returns json string converted from a python object'''
    return json.dumps(my_str)
