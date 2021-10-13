#!/usr/bin/python3
"""module that contains a function that adds a new
attribute to an object if possible"""


def add_attribute(obj, name, att):
    """function that tries to add attribute to class"""
    if hasattr(obj, "__module__"):
        setattr(obj, name, att)
    else:
        raise TypeError("can't add new attribute")
