#!/usr/bin/python3
'''python module that fetches url with urllib and prints it'''
import urllib.parse
import urllib.request
import sys
if __name__ == '__main__':
    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(e.reason)
