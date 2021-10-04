#!/usr/bin/python3
""" Module that contains a function that takes text and adds indentation """


def text_indentation(text):
    """text_indentation: function that prints indented text
    parameters:
        text: text to be indented
    Raised:
        TyperError: if text is not string type
    """
    match = "?.:"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    #parse thru str and print newline everytime \n.?:
    #and skip one index when match to skip printing said match
    for idx in range(len(text)):
        print(text[idx], end="")
        if text[idx] == "\n" or text[idx] in match:
            print("\n")
            idx += 1

