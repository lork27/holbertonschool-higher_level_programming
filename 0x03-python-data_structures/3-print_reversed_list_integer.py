#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for length in range(len(my_list) - 1, - 1, - 1):
            print("{:d}".format(my_list[length]))
