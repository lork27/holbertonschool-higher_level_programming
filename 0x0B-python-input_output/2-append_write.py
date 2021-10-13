#!/usr/bin/python3
'''module contains append_write function'''


def append_write(filename='', text=''):
    '''appends string at the end of a text file'''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
