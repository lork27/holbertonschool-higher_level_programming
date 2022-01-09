#!/usr/bin/python3
'''python module that fetches url with urllib and prints it'''
import requests
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    try:
        print(r.headers['X-Request-Id'])
    except:
        print(None)
