#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    num = -1

    for i in str:
        num += 1
        if num == n:
            pass
        else:
            newstr += i
    print('{}'.format(newstr), end='')
