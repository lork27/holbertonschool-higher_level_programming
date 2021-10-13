#!/usr/bin/python3
'''this module contains the write_file function'''


def write_file(filename="", text=""):
    '''this function writes string to a text file'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
