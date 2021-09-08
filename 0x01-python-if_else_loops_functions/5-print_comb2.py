#!/usr/bin/python3
for i in range(0, 101):
    if i < 10:
        print('0{:d}'.format(i), end='')
    else:
        print('{:d}'.format(i), end='')
    if i != 100:
        print(end=', ')
    else:
        print()
