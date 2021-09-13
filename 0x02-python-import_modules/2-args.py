#!/usr/bin/python3
import sys
length = len(sys.argv)
if len(sys.argv) <= 1:
    print("{} arguments.".format(0))
elif length > 2:
    print("{} arguments:".format(length - 1))
    for i in range(1, length):
        print("{}: {}".format(i, sys.argv[i]))
else:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
