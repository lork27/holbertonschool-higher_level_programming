#!usr/bin/python3

""" Module that contains a function that prints a formated string """

def say_my_name(fist_name, last_name=""):
    """say_my_name: function that prints formated string
    parameters:
        first_name: first string that should contain a name
        last_name: second string that should contain a last name, empty string if argument not passed
    Raised:
        TypeErrof: if either parameter is not str
    """
    if first_name is not str:
        raise TypeError("first_name must be a string")
    if last_name is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
