#!/usr/bin/python3
'''python module that fetches url with urllib and prints it'''
import urllib.parse
import urllib.request
import sys
if __name__ == '__main__':
    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.urlopen(url) as response:
            print(response.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.reason))
