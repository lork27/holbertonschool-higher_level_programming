#!/usr/bin/env python3
def uppercase(str):
    upper = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            upper += chr(ord(i) - 32)
        else:
            upper += i
    print('{}'.format(upper))
