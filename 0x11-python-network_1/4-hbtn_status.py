#!/usr/bin/python3
'''python module that fetches url with urllib and prints it'''
import requests
if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    print("""Body response:
        - type: {}
        - content: {}""".format(
        type(r.text), r.text))
