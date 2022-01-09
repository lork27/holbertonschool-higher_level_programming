#!/usr/bin/python3
'''python module that fetches url with urllib and prints it'''
import requests
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    r = requests.post(url, email)
    print(r.text)
