#!/usr/bin/python3
import sys
length = len(sys.argv)
if len(sys.argv) <= 1:
    print("{:d} arguments.".format(length))
else:
    print("{:d} arguments:".format(length - 1))
    for i in range(1, length):
        print("{}: {}".format(i, sys.argv[i]))
