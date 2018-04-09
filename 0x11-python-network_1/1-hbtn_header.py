#!/usr/bin/python3
"""
Python script that fetches URL prints out header
"""

import sys
from urllib import request


def get_url(URL):
    """
    prints out header value
    """
    with request.urlopen(URL) as response:
        header = dict(response.info())
        print("{}".format(header.get('X-Request-Id')))


if __name__ == "__main__":
    get_url(sys.argv[1])
