#!/bin/usr/python3
'''module contains from_json_string function'''
import json


def from_json_string(my_str):
    '''returns object made out of a json string'''
    return json.loads(my_str)
