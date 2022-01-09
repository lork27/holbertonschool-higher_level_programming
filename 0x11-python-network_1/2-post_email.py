#!/usr/bin/python3
'''python module that fetches url with urllib and prints it'''
import urllib.parse
import urllib.request
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('utf8')
    response = urllib.request.Request(url, data)
    with urllib.request.urlopen(response) as file:
        html = file.read().decode('utf-8')
        print(html)
