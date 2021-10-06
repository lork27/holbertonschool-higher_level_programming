#!/usr/bin/python3

""" Module that contains a function that prints a formated string """


def say_my_name(first_name, last_name=""):
    """comment"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
