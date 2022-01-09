#!/usr/bin/python3
'''python module that fetches url with urllib and prints it'''
import urllib.request
if __name__ == '__main__':
    url = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("""Body response:
        - type: {}
        - content: {}
        - utf8 content: {}""".format(
            type(html), html,
            html.decode('utf8')))
