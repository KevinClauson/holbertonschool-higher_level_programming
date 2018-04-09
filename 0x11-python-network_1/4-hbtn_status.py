#!/usr/bin/python3
"""
Python script that fetches URL
"""

import requests


URL = 'https://intranet.hbtn.io/status'


def get_url():
    """
    gets url
    """
    r = requests.get(URL)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))

if __name__ == "__main__":
    get_url()
