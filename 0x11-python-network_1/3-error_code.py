#!/usr/bin/python3
"""
Python script that makes get request
"""

import sys
from urllib import request, error


def get_url(url):
    """
    prints out response and covers for error cases
    """
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            resp = response.read()
        print("{}".format(resp.decode('utf8')))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    get_url(sys.argv[1])
