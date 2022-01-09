#!/usr/bin/python3
'''python module that fetches url with urllib and prints it'''
import urllib.request
import sys
if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.getheader('X-request-Id')
        print(html)
