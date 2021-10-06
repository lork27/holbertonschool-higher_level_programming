#!/usr/bin/python3
""" Module that contains a function that takes text and adds indentation """


def text_indentation(text):
    """comment"""
    match = ".?:\n"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    idx = 0

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] in match:
            print("\n")
            while(text[idx + 1] == ' '):
                idx += 1
        idx += 1
