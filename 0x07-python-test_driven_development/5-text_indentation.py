#!/usr/bin/python3


def text_indentation(text):
    if text is not str:
        raise TypeError("text must be a string")

    idx = 0
    #parse thru str and print newline everytime \n.?:
    #and skip one index when match to skip printing said match
