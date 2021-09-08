#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        n = number % -10
        n = abs(n)
        print('{:d}'.format(n))
        return(n)
    else:
        n = number % 10
        print('{:d}'.format(n))
        return(n)
