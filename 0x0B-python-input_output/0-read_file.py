#!/usr/bin/python3
'''this module contains the read_file function'''


def read_file(filename=""):
    '''function that reads a text file'''
    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        print(f.read(), end="")
