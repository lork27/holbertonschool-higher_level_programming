#!/usr/bin/python3
'''python module that fetches
url with urllib and prints it'''
import requests
import sys
if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(user, passwd))
    print(r.json().get('id'))
