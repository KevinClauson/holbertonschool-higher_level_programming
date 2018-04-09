#!/usr/bin/python3
"""
Python script that fetches URL prints out header
"""

import sys
import requests


def get_url(URL):
    """
    prints out header value
    """
    r = requests.get(URL)
    print("{}".format(r.headers.get('X-Request-Id')))

if __name__ == "__main__":
    get_url(sys.argv[1])
