#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length <= 1:
        length -= 1
        print("{} arguments.".format(length))
    elif length > 2:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("1 argument:")
        print("{}: {}".format(length - 1, sys.argv[1]))
