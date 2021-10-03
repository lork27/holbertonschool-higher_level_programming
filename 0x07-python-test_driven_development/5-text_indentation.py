#!/usr/bin/python3


def text_indentation(text):
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

