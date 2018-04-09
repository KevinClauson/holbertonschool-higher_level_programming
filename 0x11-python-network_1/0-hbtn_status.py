#!/usr/bin/python3
"""
Python script that fetches URL
"""

from urllib import request


URL = 'https://intranet.hbtn.io/status'


def get_url():
    """
    gets url
    """
    with request.urlopen(URL) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))

if __name__ == "__main__":
    get_url()
