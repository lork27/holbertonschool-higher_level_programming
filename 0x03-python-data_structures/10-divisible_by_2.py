#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    leng = len(my_list)
    new_list = [False] * leng
    for i in range(leng):
        if my_list[i] % 2 == 0:
            new_list[i] = True
    return new_list
