#!/usr/bin/python3
'''module that contains load_from_json_file function'''
import json


def load_from_json_file(filename):
    '''creates object out of text file with JSON string'''
    with open(filename, 'r') as f:
        return json.loads(f.read())
