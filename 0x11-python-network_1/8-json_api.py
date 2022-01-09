#!/usr/bin/python3
'''python module that fetches
url with urllib and prints it'''
import requests
import sys
if __name__ == '__main__':
    try:
        jsonquery = {"q": sys.argv[1]}
    except:
        jsonquery = {"q": ""}
    url = 'http://0.0.0.0:5000/search_user'
    try:
        r = requests.post(url, jsonquery)
        if (r.json().get('id') is not None):
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
