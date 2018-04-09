#!/usr/bin/python3
"""
Python script that makes get request
"""

import sys
import requests


def get_url(url):
    """
    prints out response and covers for error cases
    """

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))

if __name__ == "__main__":
    get_url(sys.argv[1])
